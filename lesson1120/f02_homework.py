# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : f02_homework.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2022/11/20 9:50
# @Copyright: 北京码同学

"""
2.需要你写一个函数，这个函数有一个string类型的入参， 这个函数所做的事情，就是找出入参当中所有包含的子串 （例如：abcdcccabcc是入参，bcd、bc都是子串，ac不是，包含关系，最少2个字符），
并统计每一种子串在入参当中出现的次数，降序输出，例如ab出现了2次。

子串：按照题目要求，最少两个连续的字符才算是子串
"""
"""
先找子串：abcdcccabcc
从第一个a开始：
ab([0:2])、abc([0:3])、abcd([0:4])、abcdc([0:5])... abcdcccabcc([0:11])
从第二个b开始：
bc([1:3])、bcd([1:4])、bcdc([1:5])、bcdcc([1:6])... bcdcccabcc([1:11])
从第三个c开始：
cd([2:4])、cdc([2:5])、cdcc([2:6])、cdccc([2:7])... cdcccabcc([2:11])
....
从倒数第三个b开始
bc([8:10])、bcc([8:11])
通过观察，我们发现，切片中的开始索引和结束索引都是有规律，而且都是不断变化的
要想完成两组数据的变化，需要借助两层循环
"""


def find_sub_sort(s:str):
    # 定义一个字典，把每一个子串当做字典的key，把他的次数当做value
    sub_dict = {}
    for i in range(len(s)):# 注意这个i就是上面分析时的每个切片的开始索引
        for j in range(i+2,len(s)+1):# j在这里代表上面分析时的每个切片的结束索引
            sub_str = s[i:j] # 通过切片得到每个字符串
            # s.count(sub_str) # 注意这个方法在统计时，可能达不到咱们这个题目的预期
            # 判断子串是否已经在sub_dict，如果不在的话就追加到字典，次数为1
            # 如果已经存在，那么就是用原来的次数再加1
            if sub_str in sub_dict:
                sub_dict[sub_str] = sub_dict[sub_str]+1
            else:
                sub_dict[sub_str] = 1
    print(sub_dict)
    # 针对统计得到的字典进行排序，按照字典的value，降序输出
    print(sorted(sub_dict.items(), key=lambda item: item[1],reverse=True))

if __name__ == '__main__':
    s = 'abcdcccabcc'
    # print(s.count('cc'))
    find_sub_sort(s)
    d1 = {'a':1,'b':2}
    # 动态追加或者修改字典数据
    d1['c']=2
    print(d1)
    d1['a'] = d1['a']+1
    print(d1)