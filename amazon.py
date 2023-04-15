import requests
from lxml import html
import subprocess
import sys

from email.message import EmailMessage
from password import *
import sys
import time

def get_price(link):
    try:
        url = link
        headers = {
            'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'Accept-Encoding': None
        }

        r = requests.get(url,headers=headers)
    except:
        subprocess.run(['python3','error.py',email])
        tree = html.fromstring(r.content)
        price = tree.xpath('//span[@class="a-price-whole"]/text()')[0]
        display_price = price
        print(price)
        return display_price


if __name__ == "__main__":
    while(True):
        link = sys.argv[1]
        email = sys.argv[2]
        app = sys.argv[3]
        display_price = get_price(link)
        display_price = '₹'+display_price
        price = display_price.replace('₹','')
        price = price.replace(',','')
        if float(price) < 1000000:
            subprocess.run(['python3','new_script.py',link,email,app,display_price])   
        
        
        
