import web

db = web.database(
        dbn='mysql',
        host='localhost',
        port=8080,
        user='root',
        passwd='123',
        db='book',
        charset='utf8')
urls = (
    '/', 'Index',
)

class Index(object):
    def GET(self):
        i = web.input()
        id = i.get("id", 1)
        data = db.query("select * from books where id=%s"%id)
        data = data[0]
        return data['content']
if __name__ == '__main__':
    web.application(urls, globals()).run()
