__author__ = "紫羽"

from tkinter import *
import requests
from tkinter import messagebox
import re
from PIL import Image,ImageTk

def download():
    startUrl = 'http://www.uustv.com'
    name = entry.get()
    if not name:
        messagebox.showinfo('提示', '请输入名字')
    else:
        data = {
            'word': name,
            'sizes': 60,
            'fonts':'jfcs.ttf',
            'fontcolor':'#000000'
        }
        result = requests.post(startUrl,data=data)
        result.encoding = 'utf-8'

        req = '<div class="tu"><img src="(.*?)"/></div>'
        imgUrl = startUrl + (re.findall(req,result.text)[0])
        response = requests.get(imgUrl).content
        with open('{}.gif'.format(name), 'wb')as f:
            f.write(response)


root = Tk()
root.geometry('600x300+500+300')
label = Label(root,text='签名', font=('华文行楷',20,),fg='red')
label.grid()
mainloop()