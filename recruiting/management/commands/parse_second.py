from django.core.management.base import BaseCommand
from pyquery import PyQuery as pq
import requests
from lxml import etree
import os
from django.conf import settings
from urllib.parse import urljoin

from recruiting.models import Company, Vacancy

# DOMAIN = 'http://www.meinpraktikum.de/'
SITE_URL = 'http://www.meinpraktikum.de/praktikum/kindernothilfe-e-v/praktikumsstellen/'
# VACANCY_LIST_URLPATH = '/praktikum/suchen/'


class Command(BaseCommand):

    # def parse_jobs(self, d, root, company_obj):
    #     jobs = d.items()
    #     for job in jobs:
    #         job_url = job.find('a.title').attr('href')
    #         r3 = requests.get(urljoin(DOMAIN, job_url), headers=HEADERS)
    #         d3 = pq(r3.text)
    #
    #         vacancy_title = d3.find('div.paper-sheet').find('h2').remove('span').text()
    #         vacancy_description = ''
    #         if d3.find('div.info.info-imported-aldi-sued'):
    #             vacancy_description = d3.find('div.info.info-imported-aldi-sued').html()
    #         elif d3.find('div.wysiwyg'):
    #             vacancy_description = d3.find('div.wysiwyg').html()
    #         elif d3.find('div.info.info-imported-bertelsmann'):
    #             vacancy_description = d3.find('div.info.info-imported-bertelsmann').html()
    #         elif d3.find('div.info.info-imported-ernst-young'):
    #             vacancy_description = d3.find('div.info.info-imported-ernst-young').html()
    #         elif d3.find('div.info.info-imported-ernst-young'):
    #             vacancy_description = d3.find('div.info.info-imported-ernst-young').html()
    #         else:
    #             print('Missed description for {}'.format(job_url))
    #
    #         Vacancy.objects.create(title=vacancy_title[:254],
    #                                starts_at='None',
    #                                ends_at='None',
    #                                description=vacancy_description,  # html to markdown
    #                                company=company_obj)
    #
    #         images = d3('div.images-mashup').find('img').items()
    #         images_list = []
    #         for img in images:
    #             src = img.attr('src')
    #             img_big = src.replace('small_', '')
    #             images_list.append(img_big)
    #
    #         vac = etree.SubElement(root, 'position')
    #         etree.SubElement(vac, 'identifier').text = urljoin(DOMAIN, job_url)
    #         etree.SubElement(vac, 'title').text = vacancy_title
    #         etree.SubElement(vac, 'start_date').text = ''
    #         etree.SubElement(vac, 'kind').text = 'TRAINEE'
    #         etree.SubElement(vac, 'link').text = urljoin(DOMAIN, job_url)
    #         etree.SubElement(vac, 'description').text = etree.CDATA(vacancy_description)  # markdown
    #         etree.SubElement(vac, 'top_location').text = ''
    #         etree.SubElement(vac, 'locations').text = ''
    #         images_el = etree.SubElement(vac, 'images')
    #         for image_url in images_list:
    #             etree.SubElement(images_el, 'image').text = image_url
    #         company_el = etree.SubElement(vac, 'company')
    #         etree.SubElement(company_el, 'name').text = company_obj.name
    #         etree.SubElement(vac, 'contact_email').text = ''

    # def try_next_jobs_page(self, url, root, company_obj):
    #     r = requests.get(url, headers=HEADERS)
    #     if r.status_code == 200:
    #         d = pq(r.text)
    #         if d('li.job'):
    #             self.parse_jobs(d('li.job'), root, company_obj)

    # def parse_next_block(self, url, root):
    #     r = requests.get(url, headers=HEADERS)
    #     json_data = r.json()
    #     html_results = json_data['htmlResults']
    #     d = pq(html_results)
    #     companies_list = d('.search-result').items()
    #     for item in companies_list:
    #         company_link = item.find('.search-result-vacancies-box') \
    #             .find('a.search-result-show-more').attr('href')
    #         company_name = item.find('a.search-result-headline').find('h2').text()
    #         company_obj, created = Company.objects.get_or_create(name=company_name)
    #
    #         # GET JOBS
    #         full_company_url = urljoin(DOMAIN, company_link)
    #         r2 = requests.get(full_company_url, headers=HEADERS)
    #         if r2.status_code == 200:
    #             d2 = pq(r2.text)
    #             self.parse_jobs(d2('li.job'), root, company_obj)
    #             next_page = 2
    #             pages = len(d2('nav.pagination').find('span.page'))
    #             print('pages', pages, company_link)
    #             while next_page < pages:
    #                 next_page_url = urljoin(full_company_url, '?page={}'.format(next_page))
    #                 print(next_page_url)
    #                 self.try_next_jobs_page(next_page_url, root, company_obj)
    #                 next_page += 1
    #
    #     return json_data['moreAvailable']

    def handle(self, *args, **options):
        # root = etree.Element('positions')
        # current = 0
        # step = 20
        # json_url_base = 'http://www.meinpraktikum.de/ajax_search?utf8=%E2%9C%93&q=&location=&radius=50&skip='
        #
        # more_available = self.parse_next_block(json_url_base + str(current), root)
        # print(more_available)
        # while more_available:
        #     print('+20')
        #     current += step
        #     json_url_next = json_url_base + str(current)
        #     more_available = self.parse_next_block(json_url_next, root)
        #
        # filepath = os.path.join(settings.MEDIA_ROOT, 'test.xml')
        # tree = etree.ElementTree(root)
        # tree.write(filepath, pretty_print=True, xml_declaration=True,
        #            encoding='utf-8')
        r = requests.get(SITE_URL)
        d = pq(r.text)
        # parse_jobs(d('li.job'), root, company_name)
        jobs = d('li.job').items()
        # print(len(jobs))
        for job in jobs:
            if job.find('div.date'):
                # start_date_text = job.find('div.date').remove('div.icon').text()
                print(job.find('div.date').remove('div.icon').text())
            print('----')




