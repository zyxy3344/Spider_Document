__author__ = "紫羽"

from python.Spider.Spider import base
import requests
def zhihulogin():
    sess = requests.Session()
    html = sess.base.loadpage("https://www.zhihu.com/#signin")
