# -*- coding: utf-8 -*-
#使用setdefault()和defaultdict()处理缺失的键
periodict_table = {'Hydrogen':1,'Helium':2}   #创建一个字典
print(periodict_table)

#如果键不在字典中，新的默认值会被添加进去
carbon = periodict_table.setdefault('Carbon',12)
print(carbon)
print(periodict_table)

#如果试图把一个不同的默认值赋给已经存在的键，不会改变原来的值，仍将返回初始值
helium = periodict_table.setdefault('Helium',947)   #仍然输出以前的值2，而不会输出947
print(helium)
print(periodict_table)

#defaultdict()也有同样的用法，但是创建字典时，对每个新的键都会指定默认值，它的参数是一个函数
#在本列中，把函数int作为参数传入，会按照int()调用，返回整数0
from collections import defaultdict
periodict_table = defaultdict(int)
#现在任何缺失的值都会被赋值为0
periodict_table['hydrogen'] = 1
periodict_table['Lead']       #Lead含缺失值，赋为0
print(periodict_table)

#函数defaultdict（）的参数是一个函数，他返回缺失键的值
#在下面的列子中，no_idea()在需要时会被执行，返回一个值
from collections import defaultdict
def no_idea():
    return 'Huh?'
bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable snowman'
bestiary['B'] = 'Basilisk'
print(bestiary['A'])
print(bestiary['B'])
print(bestiary['C'])
#同样，可以使用int()，dict(），list()分别返回0，空字典{}，空列表[],如果删掉该函数的参数，新建的初始值会被设置为None


bestiary1 = defaultdict(lambda:'HUH?')
#等价于：
def bestiary1():
    return 'HUN?'
print(bestiary1())

#使用int是一种定义计数器的方式
from collections import defaultdict
food_counter = defaultdict(int)
for food in ['spam','spam','egg','spam']:
    food_counter[food] += 1
for food,count in food_counter.items():
    print(food,count)

#普通字典的写法
dict_count = {}
for food in ['spam','spam','egg','spam']:
    if not food in dict_count:
        dict_count[food] = 0
    dict_count[food] += 1
for food,count in dict_count.items():
    print(food,count)

