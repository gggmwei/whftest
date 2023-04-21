# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : f04_package_module_import.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2022/11/20 11:29
# @Copyright: 北京码同学

# 模块：最简单的理解一个py文件就是一个模块
# 包：具有__init__.py文件的目录就是一个包，按照一定的业务分类去管理n多的模块


# 如果我们要跨包或者模块去使用一些方法，那么需要先导入对应的方法
# 我想调用f02_homework.py中的find_sub_sort函数
from f02_homework import find_sub_sort
from lesson1120.f03_jicheng import Cat

find_sub_sort('shdhhfghsyeq6e6qmn')

# 我想调用lesson1113下的f13_face_to_object_study.py 里边的类Plane
from lesson1113.f13_face_to_object_study import Plane
p1 = Plane(length=110,width=35,height=70,sn='f001')
p1.fly()

# as的用法，起别名
# 当在同一个文件中，需要导入的内容来自于不通的地方，但是他们的名字相同，此时需要起别名来区分他们
# 当你导入的内容名字很长时，你想简化他在当前文件的使用，可以起别名
from f01_homework import Student as Stu1
stu1 = Stu1(name='张三',age=18,banji='python自动化1030')


# 自动导入，先写目标函数或者类的名字，此时代码会报红色线，光标放在红色线上，点键盘上的alt+enter,会自动提示导入，然后选择即可
cat1 = Cat(name='咖啡猫',color='咖啡色')

from study import *

# 标识符  说白了，就是各种各样的名字，比如包名称、模块名称、变量名称、函数名称、方法名称、类名称

# 内置关键字 不能作为标识符，内置关键字意思就是被python征用了的一系列单词
A=1
a=2


# 如果你这个目录放的都是代码，那么用包
# 如果你这个目录里放的就是普通文件，那么用目录

