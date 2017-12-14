from distutils.core import setup
#安装hello模块
setup(name='Hello',version='1.0',description='A simple example',author='self',py_modules=['hello'])
#参考打包目录
#运行 python setup.py build 将在当前目录创建build目录将模块构建到lib下
#运行 python setup.py install （安装到本地变量）根据PYTHONONPATH变量 会将模块拷贝到Lib\site-packages目录下，同时生成egg_info信息（包含内容如下）
# Metadata-Version: 1.0
# Name: Hello
# Version: 1.0
# Summary: A simple example
# Home-page: UNKNOWN
# Author: self
# Author-email: UNKNOWN
# License: UNKNOWN
# Description: UNKNOWN
# Platform: UNKNOWN
#运行 python setup.py sdist （创建压缩包）可以添加文件（查看MANIFEST.in include默认添加README.txt）
#运行 python setup.py bdist （创建压缩包）可以添加文件（查看MANIFEST.in include默认添加README.txt）



