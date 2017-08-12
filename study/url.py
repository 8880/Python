#coding=utf-8
import urllib
import re

def getlist():
    html = urllib.urlopen('http://www.quanshuwang.com/book/9/9055/')
    html = html.read()
    text = html.decode('gb2312').encode('utf8')
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    return re.findall(reg, text)

def getconnect(url):
    html = urllib.urlopen('http://www.quanshuwang.com/book/9/9055/'+url).read()
    text = html.decode('gbk').encode('utf8')
    reg1 = r'</em><strong class="l jieqi_title">(.*?)</strong>'
    reg = r'&nbsp;&nbsp;&nbsp;&nbsp;([^<]*)'
    r1 = re.findall(reg1, text)
    r = re.findall(reg,text)
    print r1[0]
    for i in r:
        f1 = open(r1[0],'a')
        f1.writelines(i+'\n')
    f1.close()

for i in getlist():
    getconnect(i[0])
