#coding=utf-8
import urllib
import re
import MySQLdb

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
    reg = r'style5\(\);</script>((.|\n)*?)<script type="text/javascript">'
    reg = re.compile(reg)
    r1 = re.findall(reg1, text)
    b = re.findall(reg,text)[0]
    print r1[0]
    return b[0]

class Sql(object):
    db = MySQLdb.connect('localhost','root','123','book',charset='utf8')

    def insert(self,title,content):
        cur = self.db.cursor()
        cur.execute('insert into books values(NULL, "%s", "%s")'%(title, content))
        cur.close()
        self.db.commit()

mysql = Sql()

for i in getlist():
    title = i[1]
    content = getconnect(i[0])
    mysql.insert(title, content)
    break
