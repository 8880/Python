#coding=utf-8
f = open('file',"r+")

s = f.read(6)

print f.tell()
f.seek(6)
f.seek(6,1)       #默认值为 0，代表从文件开头算起，1代表从当前位置算起，2 代表从文件末尾算起。
f.seek(-7,2)
print f.read(6)
