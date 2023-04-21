# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : f03_jicheng.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2022/11/20 10:40
# @Copyright: 北京码同学


# 下面的Cat和Dog类的构造函数一模一样，所以我们可以向上抽取他们公共的父类啥
# 然后通过继承的方式，简化代码的维护和编写

class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self,s):
        print(f'{self.name} 吃 {s}')

class Cat(Animal):# 括号里写了Animal，说明Cat继承了Animal
    # pass
    # def __init__(self,name):
    #     self.name = name
    # 如果子类还具备除了父类定义的初始化内容以外，还有自己特殊的属性时，可以再次定义构造函数
    def __init__(self,name,color):
        super().__init__(name) # 调用父类构造函数，继承先辈定义
        # super(Cat, self).__init__()
        # self.name = name
        self.color = color

    # def eat(self,s):
    #     print(f'{self.name} 吃 {s}')
    # 这种现象就叫做多态，多态指的就是相同的事物有不同的表现形态
    def eat(self,s,n):# 当自己的方法和父类方法同名时，该对象调用时调用的自己的
        print(f'{self.name} 吃了 {n} 个 {s}')

class Dog(Animal):# 括号里写了Animal，说明Dog继承了Animal
    # def __init__(self,name):
    #     self.name = name
    pass
    # def eat(self,s):
    #     print(f'{self.name} 吃 {s}')
class MyOrderList:
    def user_info(self):
        pass
    pass

if __name__ == '__main__':
    cat1 = Cat(name='咖啡猫',color='咖啡色')
    print(cat1.name)
    print(cat1.color)
    cat1.eat('鱼',2)