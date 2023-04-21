# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : f01_homework.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2022/11/20 9:33
# @Copyright: 北京码同学


"""
一、作业
1.参考课件中的学生类去创建学生类，并实例化两个对象
2.需要你写一个函数，这个函数有一个string类型的入参， 这个函数所做的事情，就是找出入参当中所有包含的子串 （例如：abcdcccabcc是入参，bcd、bc都是子串，ac不是，包含关系，最少2个字符），
并统计每一种子串在入参当中出现的次数，降序输出，例如ab出现了2次。
"""
class Student:

    # 学生对象与生俱来就必须具备 姓名、年龄、班级 这三个属性
    def __init__(self,name,age,banji):
        self.name = name
        self.age = age
        self.banji = banji

    def print_name(self):
        print(self.name)
    def print_age(self):
        print(self.age)
    def set_name(self,name):
        self.name = name
    def print_banji(self):
        print(self.banji)
if __name__ == '__main__':
    stu1 = Student(name='张三',age=18,banji='python自动化1030')
    stu1.print_name()
    stu1.print_age()
    stu1.print_banji()
    stu2 = Student(name='李四', age=20, banji='python自动化1030')
    stu2.print_name()
    stu2.print_age()
    stu2.print_banji()
    stu2.set_name(name='李四四')
    stu2.print_name()

