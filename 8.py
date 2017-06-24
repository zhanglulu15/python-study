# -*- coding: utf-8 -*-
# import sys
# print('Program arguments:',sys.argv)
#
#
#
#
#
#
# def get_descripton():
#     """Return random weather,just like the pros"""
#     from random import choice
#     possibilities = ['rain','snow','sleet','fog','sun','who knows']
#     return choice(possibilities)
# print("Taday's weather:" , get_descripton())
#
#
# def get_description():
#     import random    #random在函数内部
#     possibilities = ['rain','snow','sleet','fog','sun','who knows']
#     return random.choice(possibilities)
# print("Taday's weather:" + get_descripton())
#
#
#
# import random #random在函数外部
# def get_description():
#     possibilities = ['rain','snow','sleet','fog','sun','who knows']
#     return random.choice(possibilities)
# print("Today's weather:" + get_descripton())
#
#
#
# #使用别名导入模块
# import random as wr
# def get_description():
#     possibilities =  ['rain','snow','sleet','fog','sun','who knows']
#     return wr.choice(possibilities)
# print("Today's weather:" + get_descripton())
#

#模块搜索路径
# import sys
# for place in sys.path:
#     print(place)
#

#包
# from sources import daily, weekly
# print("Daily forecast:",daily.forecast())
# print("Weekly forecast:")
# for number,outlook in enumerate(weekly.forecast(),1):
#     print(number,outlook)
# def forecast():
#     'fake daily forecast'
#     return 'like yestday'
# def forecast():
#     """Fake weekly forecast"""
#     return ['snow','more snow','sleet','freezing rain','rain','fog','hail']
#