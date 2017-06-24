print('%s' % 42)  #输出字符串类型
print('%d' % 42)  #十进制整数
print('%d%%' % 100)   #文本值本身

actor = 'richard gere'
cat = 'chester'
weight = 28
print("my wife's favorite actor is %s" % actor)    #字符串类的%s意味着需要插入一个字符串，字符串中出现%的次数需要与%之后所提供的
                                                   #整数项个数相同
print("our cat %s weighs %s pounds" % (cat,weight))    #如果需要插入多个数据，则需要将它们封装在一个元组当中


#使用match()进行准确匹配:只能检测以模式串作为开头的源字符串
import re
source = 'young frankenstein'
m = re.match('you',source)    #从源字符串的开头开始匹配
if m:                         #匹配成功返回了对象，将它输出看看匹配得到的到底是什么
    print(m.group())




import re
source = 'young frankenstein'
m = re.search('frank',source)  #search（）可以检测任何位置的匹配
if m:
    print(m.group())

m = re.match('.*frank',source)
if m :  #match返回对象
    print(m.group())

# .代表任何单一字符
# *代表任意一个它之前的字符， .*代表任意多个字符（包括0个）
# frank是我们想要在源字符串中某处进行匹配的短语

#使用search()寻找首次匹配
m = re.search('frank',source)
if m:   #search返回对象
    print(m.group)

#使用fidall()寻找所有匹配
m = re.findall('n',source)
print(m)
print('found',len(m),'source')


m = re.findall('.n',source)   #n前加上一个.匹配时加上前面的一个字母，n后面加上一个. 则匹配时后面加上一个字母
print(m)
print('found',len(m),'source')


#使用split()按匹配切分
m = re.split('n',source)
print(m)   #split返回的列表

import string
printable = string.printable
print(len(printable))
print(printable[50:])

print(re.findall('\d',printable))  #哪些字符是数字
print(re.findall('\w',printable))  #哪些是数字，字符，下划线
print(re.findall('\s',printable))  #哪些是空格符


source = '''I wish I may, I wish I might have a dish of fish tonight'''
print(re.findall('wish',source))
print(re.findall('wish|fish',source))
print(re.findall('^wish',source))
print(re.findall('^I wish',source))
print(re.findall('fish $',source))
print(re.findall('fish tonight.$',source))