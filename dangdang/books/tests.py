# from django.test import TestCase

# Create your tests here.
import requests
from lxml import etree
def funs():
    lists=[]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    for i in range(1,12):
        url = 'https://book.dangdang.com/list/newRelease_C01.54_P{}.htm'.format(i)

        wood = requests.get(url=url, headers=headers)
        # with open('wa.html','w',encoding='utf-8') as f:
        #     f.write(wood.text)

        woo = wood.text
        wo = etree.HTML(woo)
        all_list = wo.xpath('//div[@id="right"]/div[1]/div[@class="tushu"]')

        for li in all_list:
            items = {}
            title = li.xpath('./div[2]/div[1]/a/text()')[0]
            texts = li.xpath('./div[2]/div[2]/div[1]/text()')
            text = li.xpath('./div[2]/div[2]/div[2]/text()')[0]
            name = texts[0].split("作者：")[-1].replace(" ", "")

            press_name = texts[1].split("\u3000")[0].replace(" ", "").replace("\r\n\t\t出版社：","")
            date = texts[-1].split("出版时间：")[-1].replace(" ", "")
            price = li.xpath('./div[2]/div[4]/span/span[2]/text()')[0].replace("￥", "")
            items['title'] = title
            items['text'] = text
            items['name'] = name
            items['press_name'] = press_name
            items['date'] = date
            items['price'] = price
            lists.append(items)
    return lists

import redis

wo=redis.Redis(host='127.0.0.1',port=6379)
wo.set("wo","zeng")
print(wo.get("hello"))
