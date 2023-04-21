# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : stu_db.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2022/11/20 13:49
# @Copyright: 北京码同学
from lesson1120.student import Student


class StuDBOperate:
    stu_db_file = 'students_info.txt' # 定义存储文件的路径

    # 读取数据
    @classmethod
    def read_stus(cls):
        # 读取数据后将其转变成{"1":stu1,"2":stu2,"3":stu3,"4":stu4}
        stus_dict = {}
        with open(file=cls.stu_db_file,mode='r',encoding='UTF-8') as f:
            # print(f.read())
            all_lines = f.readlines() # 按行去读，返回结果是列表
            for line in all_lines:
                # line就表示了当前行的信息
                # line = '1,沙陌,18729399607,qq27377,wx001'
                line_list = line.split(',') # 通过逗号分割字符串，得到学员的各项信息
                stu_id = line_list[0]
                name = line_list[1]
                phone = line_list[2]
                qq = line_list[3]
                wx = line_list[4]
                # 实例化这个学员对象
                stu = Student(stu_id=stu_id,name=name,phone=phone,qq=qq,wx=wx)
                stus_dict[stu_id] = stu
        return stus_dict

    # 写入数据
    @classmethod
    def write_stus(cls,stus_dict):
        # stus_dict = {"1":stu1,"2":stu2,"3":stu3,"4":stu4}
        with open(file=cls.stu_db_file,mode='w',encoding='UTF-8') as f:
            # 文件里每一行的格式是 '1,沙陌,18729399607,qq27377,wx001'
            # 所以我们要把stus_dict中的学员对象，变成字符串形式
            for stu in stus_dict.values():
                stu_str = f'{stu.get_stu_id()},{stu.get_name()},{stu.get_phone()},{stu.get_qq()},{stu.get_wx().strip()}'
                f.write(stu_str)
                f.write('\n')

if __name__ == '__main__':
    # 读取文件中的内容 每一行生成一个对象 放在stus_dict字典中
    stus_dict = StuDBOperate.read_stus()
    # 当前文件内容如下
    # 1, 沙陌, 18729399607, qq27377, wx001
    # 2, 张三, 1892882837, qq76625, wx8282
    # 3, 极光, 18729399609, qq27378,
    # 4, 半夏, 18729399610,,
    # 5, 彩虹, 1726366262,,
    print(stus_dict)
    # 测试插入
    # 新建一个对象 stu_id = 6
    stu6 = Student('6',name='google',phone='110')
    # 将新建的对象放在字典中 新对象的key=6
    stus_dict['6'] = stu6
    # 将整个字典覆盖写入文件中
    StuDBOperate.write_stus(stus_dict)
    # 然后整个文件就变成了
    # 1, 沙陌, 18729399607, qq27377, wx001
    # 2, 张三, 1892882837, qq76625, wx8282
    # 3, 极光, 18729399609, qq27378,
    # 4, 半夏, 18729399610,,
    # 5, 彩虹, 1726366262,,
    # 6, google, 110,,



    # #测试删除 将刚刚插入的stu_id = 6的对象删除了
    # del stus_dict['6']
    # # 将整个字典覆盖写入文件中
    # StuDBOperate.write_stus(stus_dict)
    #
    # #测试修改 将stu_id = 5的对象名称改为番茄
    # stu5 = stus_dict['5']
    # stu5.set_name('番茄')
    # # 将整个字典覆盖写入文件中
    # StuDBOperate.write_stus(stus_dict)