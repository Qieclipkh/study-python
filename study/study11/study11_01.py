#文件处理
import os
#打开文件，不存在抛出异常IOError，可以指定文件模式和缓冲参数
filePath = r"E:\gihub-self\study-python\study\study11\somefile.txt"
f = open(filePath,mode='a+')
f.write("hello,")
f.write(" world"+os.linesep)
f.close()

for f in open(filePath):
    print(f)




