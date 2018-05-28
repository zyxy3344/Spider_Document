__author__ = "紫羽"
from python.Spider.Spider import base
from bs4 import BeautifulSoup
import json
from lxml import etree

html = base.loadpage('https://www.qiushibaike.com/')

xml = etree.HTML(html)

node_list = xml.xpath(r'//div[contains(@id, "qiushi_tag")]')

name_list = xml.xpath(r'//div[contains(@id, "qiushi_tag")]/div/a/h2/text()')

content_list = xml.xpath(r'//div[contains(@id, "qiushi_tag")]/a/div/span/text()')

for i in range(len(name_list)):
    name = name_list[i].strip()
    content = content_list[i].strip()
    pattern = {
        'name': name,
        'content': content
    }
    with open('qiushi','a')as f:
        f.write(json.dumps(pattern, ensure_ascii=False))

# html = base.loadpage("https://www.lagou.com/lbs/getAllCitySearchLabels.json")
# base.savehtml(html)
# base.json_text(html)
# soup = BeautifulSoup(html)
# print(html.code)
