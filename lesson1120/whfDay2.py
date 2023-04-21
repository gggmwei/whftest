# 什么是运算符?有哪些运算符?
#
# 什么是条件语句(代码写一个)?条件语句什么时候成立什么时候不成立?
num=10
if num<0 or num>10:
    print('hello')
else:
    print('null')

# 有几种循环语句(分别写一个)?有哪些循环控制语句,分别是什么作用?
# while循环
# for循环
# 嵌套循环
count=0
while (count<9):
    print(count)
    count=count+1
print("sss")

i=1
while i<10:
    i +=1
    if i%2>0:
        continue
    print(i)

i=1
while 1:
    print(i)
    i+=1
    if i>10:
        break


# 写一个无限循环?


# 分别使用两种循环语句加上条件语句实现坐电梯的功能?一共有31层楼,到15楼停下,且输出“15到了,我到家了”
i=1
while i<31:
    i+=1
    if i==15:
        continue
print('15到了，我到家了')


i=1
while i<31:
    i+=1
    if i==15:
        print('15到了，我到家了')
        break



# 声明一个列表 用两种方式迭代这个序列 (索引迭代和非索引迭代)

ls = ["AAA", "BBB", "CCC", "DDD"]
for i in range(len(ls)):
    print(i + 1, ls[i])


ls = ["AAA", "BBB", "CCC", "DDD"]
for item in ls:
    print(item)



# 有两个整数a,b， a,b的取值范围在0-9之间，给出所有符合a+b=12的组合 (考的是两层嵌套循环)
#
# A、B、C、D分别为0-9之间的整数，求出满足AB+CD=DA条件的数。    例如：90+09=99  (考的是多层嵌套循环,这个难点,思考不出来先百度,晚上做题时不会给提示)
#
#
# 嵌套循环里面的break语句是终止哪一层?
#
# 声明列表,对列表进行增删改查操作,然后写几个常用的列表函数?并说出你写的函数的输出结果
list=[1,2,3,4,5]
list.append('aa')
print(list)
del list[5]
print(list)
list[0]='bb'
print(list)

#列表元素个数
print(len(list))

list1=['ww']
list.extend(list1)
print(list)

list.reverse()
print(list)

# 声明元组,写出文档中所有的元组内置函数?并说出你写的函数的输出结果
tuple1=(1,2,3,4)
tuple2=(4,5,6)

print(len(tuple1))
print(max(tuple1))
print(min(tuple1))

aa=tuple(list)
print(aa)


# 声明字典,对字典进行增删改查操作,然后写几个常用的字典函数?并说出你写的函数的输出结果
dict1={'aa':11,'bb':22}
dict1['aa']=88
dict1['school']='eee'
print(dict1)

del dict1['school']
print(dict1)


# 有元组 T1=(‘ python ’,’java ’,'web编程 ’,’机器学习 ’,’ 图像处理 ’,’ 数据结构 ’,’ java ’,’ 人工智能 ’) ，编写代码实现下面功能：
# （ 1 ）向元组添加元素‘操作系统’，是否成功
# （ 2 ）分别用 for 、 while 语句，遍历输出元组元素
# （ 3 ）统计‘java’在元组中出现的次数
# （ 4 ）查找‘数据结构’在元组中的位置
# （ 5 ）把元组转换成列表 L1
# （ 6 ）把元组转换成字符串 S
# （ 7 ）有元组 T2=(‘ 大数据 ’,’ 计科 ’,’ 软工 ’，’网工‘) ，连接元组 T1 和 T2 生成新元组 T3
T1=('python','java','web编程','机器学习')
T2=('jjj',)
T3=T1+T2
print(T1)
print(T3)



# 生成一个包含数字1,2,3,…,99的列表，输入一个2~9之间的正整数，
# 条件1:列表中元素是这个数的倍数
# 条件2:列表中元素的个位或十位上等于这个数字，
# 满足任意条件 则将这个元素添加到新的列表中 最后打印新的列表
# 例如，输入"7"，找出列表中7的倍数和数位上包含7的数，添加到新列表,再输出新列表。 提示:想拿到一个数的个位或十位是什么 会用到取模运算和除法运算
#
#
#
# 有如下字典：
# userDict = {‘admin’:‘123456’,‘administrator’:‘12345678’,‘root’:‘password’}，
# 其键和值分别代表用户名与密码，请编程实现用户登录验证。用户输入用户名和密码，当用户名与密码和字典中中的某个键值对匹配时，