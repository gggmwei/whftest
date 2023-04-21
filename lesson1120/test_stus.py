# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : test_stus.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2022/11/20 16:08
# @Copyright: 北京码同学
import unittest

# unittest的测试必须以类的形式，并且必须继承unittest.TestCase
import ddt

from lesson1120.stu_operate import StusOperate


class TestAddStu(unittest.TestCase):


    # 在该类下所有用例开始前去完成数据准备或者其他前置动作
    # 这个前置后置的名字是固定的
    @classmethod
    def setUpClass(cls) -> None:
        print('在该类下所有用例开始前去完成数据准备或者其他前置动作')
        # 先清除掉6这个学员，以防止数据不对
        StusOperate.del_stu('6')
    @classmethod
    def tearDownClass(cls) -> None:
        print('在该类下所有用例执行玩去清除或者其他后置动作')
        # z清除掉6这个学员，以防止数据不对
        StusOperate.del_stu('6')

    def setUp(self) -> None:
        # 在每一个测试用例执行开始前去执行的动作
        print('在每一个测试用例执行开始前去执行的动作')
    def tearDown(self) -> None:
        # 在每一个测试用例执行完之后去执行的动作
        print('在每一个测试用例执行完之后去执行的动作')


    # 每条用例都需要以test开头
    def test1_add_stu_id_not(self):
        # 所谓的测试，其实就是调用
        res = StusOperate.add_stu('6',name='沙陌1',phone='7612662')
        # 调用以后得到方法执行结果，然后去做结果判断
        # 针对结果做判断的过程，叫做断言
        assert res == '添加成功'
    def test2_add_stu_id_already(self):
        res = StusOperate.add_stu('6', name='沙陌1', phone='7612662')
        assert res == '6已存在，无法添加'



@ddt.ddt
class TestChangeStu(unittest.TestCase):

    # 列表套列表的形式，里边每一个列表都代表一组数据
    # 子列表中第一个数据，代表是学员id
    # 第二个列数据是个字典，代表的要修改的属性
    # 第三列数据代表的期望结果的值
    test_data = [
        ['2', {'name': '张三'}, '修改成功'],
        ['2', {'phone': '1892882837'}, '修改成功'],
        ['2', {'wx': 'wx8282'}, '修改成功'],
        ['2', {'qq': 'qq76625'}, '修改成功']
    ]
    @ddt.data(*test_data)
    def test_change_stu(self,data):
        # 注意这个data其实就是每一组数据
        stu_id = data[0]
        change_info = data[1]
        expect = data[2]
        res = StusOperate.change_stu(stu_id=stu_id,**change_info)
        assert res==expect




