#coding:utf-8

import urllib
import re 

def gethtml(html):
    list1=urllib.urlopen(html)
    list2=list1.read()
    return list2

def getpicture(html,x):
    list3=r'src="(.*?\.jpg)"'
    reg=re.compile(list3)
    result=re.findall(reg,html)
    for img in result:
        urllib.urlretrieve(img,'/Users/melvinfei/Pictures/meizitu/%s.jpg'%x)
    return x

for i in range(19,51):
    html=gethtml('http://www.mzitu.com/83148/%d'%i)
    print getpicture(html,i+178)