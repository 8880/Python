import os
k = open('/home/linux/myDir/xinwenjian','a')
b = '/home/linux/myDir'
c = os.listdir(b)
for i in c:
    d = os.path.join(b,i)
    if os.path.isdir(d):
        p = os.listdir(d)
        for j in p:
            print j
            s = os.path.join(d,j)
            l = open(s,'r')
            for z in l:
                k.write(z)
