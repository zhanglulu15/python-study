# -*- coding: utf-8 -*-
#使用Counter（）计数
from collections import Counter
breakfast = ['spam','spam','egg','spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)

#函数most_commom()以降序返回所有元素，或者给定一个数字，会返回该数字前的元素
print(breakfast_counter.most_common())

print(breakfast_counter.most_common(1))

#新建一个列表lunch和一个计数器lunch_counter
lunch = ['egg','egg','bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)


#组合计数器
print(breakfast_counter + lunch_counter)

print(breakfast_counter - lunch_counter)

print(breakfast_counter & lunch_counter)

print(breakfast_counter | lunch_counter)




#使用有序字典orderdDict()按键排序
#一个字典的键的顺序是不可知的
quotes = {
    'moe':'a wise guy huh?',
    'larry':'ow!',
    'curly':'nyuk nyuk!',
}
for stooge in quotes:
    print(stooge)

#使用OrderdDict()记忆字典添加的顺序
from collections import OrderedDict
quotes = OrderedDict([('moe','a wise guy,huh?'),
                      ('larry','ow'),
                      ('curly','nyuk nyuk'),
])
for stooge in  quotes:
    print(stooge)



#双端队列：栈+队列
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
        return True
print(palindrome('a'))
print(palindrome('raeccar'))

#快速判断回文的程序
def another_palindrome(word):
    return word == word[::-1]
print(another_palindrome('radar'))

#使用迭代器
import  itertools
for item in itertools.chain([1,2],[3,4]):   #chain()的参数是单个迭代对象
    print(item)

import itertools
for item in itertools.cycle([1,2]):   #无线循环迭代
    print(item)

from itertools import accumulate
for item in itertools.accumulate([1,2,3,4]):  #累加,python2中没有
    print(item)

import itertools
def multiply(a,b):
    return a*b
for item in itertools.accumulate([1,2,3,4],accumulate):
    print(item)

#使用pprint()友好输出
from  pprint import pprint
quotes = OrderedDict([('moe', 'a wise guy,huh?'),
                       ('larry', 'ow'),
                       ('curly', 'nyuk nyuk'),
                       ])
pprint(quotes)
print(quotes)
