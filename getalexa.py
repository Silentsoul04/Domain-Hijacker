#!/usr/bin/env python

import requests
import random
import time
import sys
import json

code_country=['AD', 'AE', 'AF', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ','BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY', 'BZ', 'CA', 'CD', 'CG', 'CH', 'CI', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FJ', 'FR', 'GA', 'GB', 'GE', 'GF', 'GH', 'GI', 'GM', 'GN', 'GP', 'GR', 'GT', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LC', 'LK', 'LR', 'LT', 'LU', 'LV', 'LY', 'MA', 'MD', 'ME', 'MG', 'MK', 'ML', 'MM', 'MN', 'MO', 'MQ', 'MR', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PR', 'PS', 'PT', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SC', 'SD', 'SE', 'SG', 'SI', 'SK', 'SN', 'SO', 'SR', 'SV', 'SY', 'TG', 'TH', 'TJ', 'TL', 'TM', 'TN', 'TR', 'TT', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VE', 'VN', 'YE', 'ZA', 'ZM', 'ZW']

dict_country = {}
for country in code_country:
    dict_country["TOP" + country]=[]
print dict_country
topsites=[]

alexa_url='http://www.alexa.com/topsites/countries;'
tedst= 'http://www.alexa.com/topsites/countries'
HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6)'
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/45.0.2454.101 Safari/537.36'),
                          'referer': 'https://mathieuchot-plassot.com'}
for country in code_country:
    for page in range(21):
        r = requests.get(url='{}{}/{}'.format(alexa_url,page,country),headers=HEADERS)
        print r.url
        if 'site-listing' in r.text:
            links=r.text.split('<a href="/siteinfo/')
            for line in links[1::]:
                dict_country["TOP"+country].append(line.split('">')[0])
            print dict_country
        time.sleep(random.randrange(15,22))
    with open("{}/{}".format(sys.path[0], 'TOP'+country),'w+') as f:
        f.write(json.dumps(dict_country["TOP" + country]))

for country,sites in a.iteritems():
    for i in sites:
        if i not in topsites:
            topsites.append(i)

with open("{}/{}".format(sys.path[0], 'TOPsites'),'w+') as f:
        f.write(json.dumps(topsites))
