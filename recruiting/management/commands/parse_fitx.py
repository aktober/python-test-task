import requests
from django.core.management import BaseCommand
from pyquery import PyQuery as pq
from furl import furl


DOMAIN = 'https://www.fitx.de'
JOBS_PATH = '/fitness-jobs'
SITE_URL = furl(DOMAIN).join(JOBS_PATH).url
COMPANY_NAME = 'FitX'
CONTACT_EMAIL = 'karriere@fitx.de'


class Command(BaseCommand):

    def handle(self, *args, **options):
        r = requests.get(SITE_URL)
        d = pq(r.text)
        jobs = d('tr.jobs_listing_list__table_row.jobs_listing_list__table_row--visible').items()
        amount = 0
        for job in jobs:
            title = job.find('a').text()
            location = job.find('.jobs_listing_list__table--place').text()
            kind = job.find('.jobs_listing_list__table--work_time').text()
            href = job.find('a').attr('href')
            link = furl(DOMAIN).join(href).url
            print(kind)

            r = requests.get(link)
            d = pq(r.text)
            description = d.find('section.jobs_detail').eq(1).html()
            # start_date = today
            amount += 1
        print('total {}'.format(amount))
