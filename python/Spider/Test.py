__author__ = "紫羽"
from Spider import base

a = base.loadpage('http://www.52ziyu.cn')
base.savehtml(a)
print(a)





