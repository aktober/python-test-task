from django.core.management.base import BaseCommand
import requests
from lxml import html

from recruiting.models import City, Company, Vacancy, VacancyImage

URL = 'https://www.trainee.de/traineestellen/'


class Command(BaseCommand):
    def handle(self, *args, **options):
        City.objects.all().delete()
        Company.objects.all().delete()
        Vacancy.objects.all().delete()
        VacancyImage.objects.all().delete()

        page = requests.get(URL)
        tree = html.fromstring(page.content)
        items = tree.xpath('//li[@class="tr-list__item"]')[:20]

        for item in items:

            title = item.xpath('.//h4[@class="tr-text-trans-none line-clamp"]/text()')[0]

            company_name = item.xpath('.//span[@class="tr-text+ tr-text+--none-responsive tr-font-family-display"]/text()')[0]

            starts_at_tmp = item.xpath('.//li[@class="tr-list__item tr-list__item--div tr-pdgr tr-pdgt- tr-relative-parent tr-pdgl+"]')[0]
            starts_at = starts_at_tmp.xpath('.//text()')[3].strip()

            city_tmp = item.xpath('.//li[@class="tr-list__item tr-list__item--div tr-pdgr tr-relative-parent tr-pdgl+"]')[0]
            city = city_tmp.xpath('.//text()')[3].strip()

            ends_tmp = item.xpath('.//li[@class="tr-list__item tr-list__item--div tr-pdgr tr-relative-parent tr-pdgl+"]')[1]
            ends_at = ends_tmp.xpath('.//text()')[3].strip()

            images = item.xpath('.//div/img[@class="tr-mrgt+"]/@src')

            # INFO FROM SUB PAGES
            DOMAIN = "https://www.trainee.de"
            link = item.xpath('.//a[@class="tr-card tr-card--link"]/@href')
            subpage = requests.get(DOMAIN + link[0])
            subtree = html.fromstring(subpage.content)
            description_tmp = subtree.xpath('//div[@class="tr-content tr-box tr-box--default tr-text+ tr-mrgb"]')[0]
            description = ''
            for desc in description_tmp.xpath('.//text()'):
                description += desc
            company_location_tmp = subtree.xpath('.//div[@class="tr-cms-reset"]/p/text()')
            company_location = ''
            for loc in company_location_tmp:
                company_location += loc

            # store data in db
            cities = []
            if ',' in city:
                for c in city.split(','):
                    if not City.objects.filter(name=c.strip()):
                        cities.append(City.objects.create(name=c.strip()))
            else:
                if not City.objects.filter(name=city):
                    cities.append(City.objects.create(name=city))

            company_exists = Company.objects.filter(name=company_name)
            if not company_exists:
                company_obj = Company.objects.create(name=company_name,
                                                     location=company_location)
            else:
                company_obj = company_exists[0]

            vacancy = Vacancy.objects.create(title=title,
                                             starts_at=starts_at,
                                             ends_at=ends_at,
                                             description=description.strip(),
                                             company=company_obj)

            for vacancy_location in cities:
                vacancy.location.add(vacancy_location)

            for image in images:
                image_file = VacancyImage.objects.create(url=image)
                vacancy.image_list.add(image_file)

        print('Total cities: {}'.format(City.objects.all().count()))
        print('Total companies: {}'.format(Company.objects.all().count()))
        print('Total vacancies: {}'.format(Vacancy.objects.all().count()))
        print('Total image files: {}'.format(VacancyImage.objects.all().count()))