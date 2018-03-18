from django.core.management import BaseCommand
import xml.etree.ElementTree as ET
import requests
import urllib

from django.utils import timezone
from xmljson import badgerfish as bf
from xmljson import parker, Parker
from json import dumps


XML_SOURCE = 'http://files.channable.com/vqaFs6_qJ5R3KSUphVm-AA==.xml'
start_date = timezone.now().strftime('%d.%m.%Y')
CONTACT_EMAIL = 'fallback@jobufo.com'


class Command(BaseCommand):
    def handle(self, *args, **options):
        r = requests.get(XML_SOURCE)

        root = ET.fromstring(r.text)
        amount = 0
        for item in root.iter('item'):
            d = bf.data(item)
            images = []
            if d['item']['image_link']:
                images.append(d['item']['image_link']['$'])

            data = {
                'identifier': d['item']['id']['$'],
                'title': d['item']['title']['$'],
                'start_date': start_date,
                'kind': d['item']['vertragsart']['$'],
                'link': d['item']['link']['$'],
                'description': d['item']['description']['$'],
                'location': d['item']['standort']['$'],
                'images': images,
                'contact_email': CONTACT_EMAIL,
                'company': {
                    'name': d['item']['unternehmen']['$'],
                    'address': {
                        'street': '',
                        'zip': '',
                        'city': d['item']['standort']['$'],
                    }
                }
            }
            print(data['kind'])
            amount += 1
        print(amount)
