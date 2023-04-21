# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : student.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2022/11/20 13:35
# @Copyright: 北京码同学


class Student:

    def __init__(self,stu_id,name,phone,qq='',wx=''):
        self.stu_id = stu_id
        self.name = name
        self.phone = phone
        self.qq = qq
        self.wx = wx
    # 通过情况下我们会针对属性提供get/set方法，就是获取属性和设置属性
    def get_stu_id(self):
        return self.stu_id
    def set_stu_id(self,stu_id):
        self.stu_id = stu_id
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    def get_phone(self):
        return self.phone
    def set_phone(self,phone):
        self.phone = phone
    def get_qq(self):
        return self.qq
    def set_qq(self,qq):
        self.qq = qq
    def get_wx(self):
        return self.wx
    def set_wx(self,wx):
        self.wx = wx