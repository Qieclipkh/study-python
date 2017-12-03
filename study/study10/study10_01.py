import  sys
import importlib

sys.path.append("F:\github\study-python\study\study10")

import study.study10.study10
#导入模块时，代码就执行
# 再次导入该模块，就不会执行，导入模块并不意味着导入时执行某些操作。它们主要用于定义，比如变量、函数和类等
#如果坚持重新载入模块，那么可以使用內importlib模块的reload
importlib.reload(study.study10.study10)

