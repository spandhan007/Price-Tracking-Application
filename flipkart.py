import requests
from lxml import html
import sys
import subprocess


def get_price(link):
    url = link
    headers = {
        'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'Accept-Encoding': None
    }

    r = requests.get(url,headers=headers)
    tree = html.fromstring(r.content)
    price = tree.xpath('//div[@class="_30jeq3 _16Jk6d"]/text()')[0]
    display_price = price
    return display_price


if __name__ == "__main__":
    link = sys.argv[1]
    email = sys.argv[2]
    app = sys.argv[3]
    display_price = get_price(link)
    price = display_price.replace('₹','')
    price = price.replace(',','')
    if float(price) < 250000:
        subprocess.run(['python3','new_script.py',link,email,app,display_price])