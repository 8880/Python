import web
from django.shortcuts import render

db = web.database(
        dbn='mysql',
        host='localhost',
        port=8080,
        user='root',
        passwd='123',
        db='book',
        charset='utf8')
urls = (
    # '/', 'Index',
    '/book/(\d+)\.html','index',
)
render = web.template.render('templates')
class Index(object):
    def GET(self):
        i = web.input()
        id = i.get("id", 1)
        data = db.query("select * from books where id=%s"%id)
        data = data[0]
        return render.index(data)
        # return data['content']
if __name__ == '__main__':
    web.application(urls, globals()).run()
