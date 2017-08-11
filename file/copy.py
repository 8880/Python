
try:
    f = open('default.jpg','r+')
    f2 = open('/home/linux/djangosite/booksite/static/default.jpg','w')
except:
    print "open failed"

while True:
    s = f.readline()
    if not s:
        break
    f2.write(s)
