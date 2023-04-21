# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : stu_operate.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2022/11/20 14:51
# @Copyright: 北京码同学
from lesson1120.stu_db import StuDBOperate
from lesson1120.student import Student


class StusOperate:
    # 定义一个类属性stus_dict,用来存储所有的业务数据，从文件中读取
    # 下述的增删改查统一都是在stus_dict字典进行操作的
    stus_dict = StuDBOperate.read_stus()

    # 新增学员
    @classmethod
    def add_stu(cls,stu_id,name,phone,qq='',wx=''):
        # 如果学员id已存在，那么不能添加
        if stu_id not in cls.stus_dict:
            # pass
            stu = Student(stu_id=stu_id,name=name,phone=phone,qq=qq,wx=wx)
            cls.stus_dict[stu_id] = stu
            # 重新写入文件
            StuDBOperate.write_stus(cls.stus_dict)
            return '添加成功'
        else:
            return f'{stu_id}已存在，无法添加'
    # 删除学员
    # 通常通过id去删除，所以把学员id作为入参进行传递
    @classmethod
    def del_stu(cls,stu_id):
        if stu_id in cls.stus_dict:
            del cls.stus_dict[stu_id]
            # 重新写入文件
            StuDBOperate.write_stus(cls.stus_dict)
            return '删除成功'
        else:
            return f'{stu_id}不存在，无法删除'
    # 查询学员
    # 通常情况下同id查询，所以把学员id作为入参
    @classmethod
    def select_stu(cls,stu_id):
        if stu_id in cls.stus_dict:
            stu = cls.stus_dict[stu_id]
            return f'{stu.get_stu_id()},{stu.get_name()},{stu.get_phone()},{stu.get_qq()},{stu.get_wx().strip()}'
        else:
            return f'{stu_id}不存在'

    # 修改学员
    # 要告诉这个方法修改的学员是谁，通过stu_id可以找到学员
    # 你还得告诉这个方法，你要修改这个学员的什么信息？name?phone?qq?wx?,并且要告诉这个属性要改成什么？
    # name='shamo1',phone='1823773',qq='sss'
    # 可以使用**kwargs来表示不确定的键值对入参
    @classmethod
    def change_stu(cls,stu_id,**kwargs):
        if stu_id in cls.stus_dict:
            stu = cls.stus_dict[stu_id] # 获取学员对象
            # 要在stu这个对象上进行修改，但是要改什么取决于传进来的kwargs
            if 'name' in kwargs:
                stu.set_name(kwargs['name'])
            if 'phone' in kwargs:
                stu.set_phone(kwargs['phone'])
            if 'qq' in kwargs:
                stu.set_qq(kwargs['qq'])
            if 'wx' in kwargs:
                stu.set_wx(kwargs['wx'])
            # 重新写入文件
            StuDBOperate.write_stus(cls.stus_dict)
            return '修改成功'
        else:
            return f'{stu_id}不存在，无法修改'