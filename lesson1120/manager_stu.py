# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : manager_stu.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2022/11/20 15:34
# @Copyright: 北京码同学


# 在这里实现和控制台的交互
from lesson1120.stu_operate import StusOperate


def run_stu_manager():

    print('=============欢迎来到码同学学员管理系统====================')
    # print('请输入操作序号: 1.新增  2.修改  3.查询  4.删除  5.退出')
    while True:
        op = int(input('请输入操作序号: 1.新增  2.修改  3.查询  4.删除  5.退出 :'))
        if op == 1:
            # stu_info = '1,沙陌,18729399607,qq27377,wx001'
            stu_info = input('请输入学员的各项信息,以逗号分割：')
            stu_info_list = stu_info.split(',')
            res = StusOperate.add_stu(stu_id=stu_info_list[0],
                                name=stu_info_list[1],
                                phone=stu_info_list[2],
                                qq=stu_info_list[3],
                                wx=stu_info_list[4])
            print(res)
        elif op == 2:
            stu_id = input('请输入你要修改的学员id:')
            change_info = input('请输入你要修改的学员信息,格式是{"name":"沙陌1"}：')
            # 尽管我们要求控制台输入时以字典方式输入，但是我们得到其实还是字符串
            # 为了将其转字典，我们使用eval
            change_info = eval(change_info)
            res = StusOperate.change_stu(stu_id=stu_id,**change_info)
            print(res)
        elif op == 3:
            stu_id = input('请输入你要查询的学员id:')
            res = StusOperate.select_stu(stu_id=stu_id)
            print(res)
        elif op == 4:
            stu_id = input('请输入你要删除的学员id:')
            res = StusOperate.del_stu(stu_id=stu_id)
            print(res)
        elif op == 5:
            print('退出成功')
            break
        else:
            print('输入的操作序号不支持')
if __name__ == '__main__':
    run_stu_manager()