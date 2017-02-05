#!/usr/bin/env python

import whois
import json
import sys
import time
from datetime import datetime          
import random

json_data=open(sys.path[0]+'/TOPFR')
data = json.load(json_data) #list

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

for sites in data:
    print sites
    if sites != '':
        site=whois.whois(sites)
        if site['registrar'] == None:
            with open(sys.path[0]+'/hidden_domains', 'w+') as f:
                f.write(sites)
        else:
            if type(site['expiration_date']) == list:
                site_expiration=site['expiration_date'][0].strftime("%Y-%m-%d")
            else:
                site_expiration=site['expiration_date'].strftime("%Y-%m-%d")
            exp_date=site_expiration.split(' ')[0]
            current_time=(time.strftime("%Y-%m-%d"))
            if days_between(current_time, exp_date) <= 7:
                with open(sys.path[0]+'/Expiresoon', 'w+') as f:
                    f.write(sites)
        time.sleep(random.randrange(20,25))
json_data.close()
