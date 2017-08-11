#coding=utf-8
import os
import shutil

# print dir(os)
#
# print "================="
#
# print dir(os.path)
#
# print "================="
#
# print dir(shutil)

print os.getcwd()

# os.remove('hold')                                  #删除

print os.path.isfile('file')                         #文件是否存在
print os.path.isdir('file')                           #文件夹是否存在
print os.path.exists('file')                         #

# print os.path.abspath(__file__)                                #查看路径
# print os.path.dirname(os.path.abspath(__file__))
# print os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print os.path.getsize('file')
#
# print os.path.join('/a/b/c','filename')             #路径拼接
#
# print os.listdir('.')                        #查看当前位置里的文件
#
# os.system('ls -l')                           #查看文件列表
# os.rename('file.py','filenew.py')             #文件改名
# os.mkdir('dir')                             #创建文件夹
#
# shutil.copyfile('file','filenew')              #复制文件
# shutil.move('a','b')                            #删除
#
# shutil.copy('a','b')                             #复制文件夹或文件
