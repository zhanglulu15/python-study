#第六章习题
#练习1:创建一个名为Thing的空类并将它打印出来，接着，创建一个属于该类的对象example,同样将它打印出来
class Thing():
    pass
print(Thing())

class Thing():
    example = Thing()               #Thing（）创建了一个Thing()类的对象，并赋值给example这个名字。由于Thing类似空的
print(Thing.example)                      #因此由它创建的对象example什么也做不了

#练习2：创建一个新类叫作：Thing2,将'abc'赋值给类特性letters,打印letters
class Thing2():
   letters = 'abc'   #将abc赋值给类的特性letters
print(Thing2.letters)


#练习3:创建一个新类Thing3,将'xyx'赋值给实例对象特性letters,并试着打印letters
#同练习2的写法
class Thing3():
    letters = 'xyz'
print(Thing3.letters)

class Thing3:
    def __init__(self):
        self.letters = 'xyz'   #将xyz赋值给实例对象的特性
#变量letters属于类Thing3的任何对象，而不是Thing类本身
#print(Thing3.letters)
someone = Thing3()             #必须创建一个对象才可以进行打印
print(someone.letters)


#练习4：创建一个名为Element的类，包含实例'name','Hydrogen','number'.使用‘Hydrogen','H','1'实例化一个对象
class Element():
    def __init__(self,name,symbal,number):
        self.name = name
        self.symbal = symbal
        self.number = number
Hydrogen = Element('Hydrogen','H','1')
print(Hydrogen.name)


#练习5:创建一个字典，包含这些键值对：name:hydrogen, symbol:H,  number:1  ，然后用这个字典实例化Element类的对象hydrogen
el_dict = {'name':'Hydrogen','symbol':'H','number':'1'}  #首先创建字典
hydrogen = Element(el_dict['name'],el_dict['symbol'],el_dict['number'])    #然后用字典实例化Element类的对象hydrogen
print(hydrogen.name)

#也可以直接从字典初始化对象，因为它的键名称是和__init__参数匹配的
# hydrogen1 = Element(**el_dict)   #**将el_dict字典中的键和值抽取出来，作为参数提供给hydrogen使用
# print(hydrogen1.name)


#练习6:为Element类定义一个dump()方法，用于打印对象的特性（name,symbol,number),使用这个新定义的类创建一个对象hydrogen并用dump()打印
class Element():
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print('name = %s,symbol = %s,number = %s' % (self.name,self.symbol,self.number))
hydrogen = Element(**el_dict)   #**将el_dict字典中的键和值抽取出来，作为参数提供给hydrogen使用
hydrogen.dump()


#练习7：调用print(hydrogen)，然后修改Element的定义，将dump方法的名字改为_str_,再次创建一个hydrogen对象
#并调用print(hydrogen),观察输出结果
class Element():
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return ('name = %s.symbol = %s,number = %s' % (self.name,self.symbol,self.number))
hydrogen = Element(**el_dict)
print(hydrogen)

#练习8:修改Element,使得name,symbol,nuber特性都变成私有的，为它定义一个getter属性（property）来返回各自的值
class Element:
    def __init__(self,name,symbol,number):
        self._name = name
        self._symbol = symbol
        self._number = number
    @property
    def name(self):
        return self._name
    @property
    def synbol(self):
        return self._symbol
    @property
    def number(self):
        return self._number
hydrogen = Element('Hydrogen','H',1)
print(hydrogen.name)
print(hydrogen.synbol)
print(hydrogen.number)


#练习9：定义三个类，Bear.Rabbit和Octothorpe，对每个类都只定义一个方法eats(),分别返回'berries'(Bear),'clover'(Rabbit)
# 和’campers'(Octothorpo)。为每个类创建一个对象并输出他们各自吃的食物（调用eats())
class Bear:
    def eats(self):
        return 'berries'
class Rabbit:
    def eats(self):
        return 'clover'
class Octothorpe:
    def eats(self):
        return 'campers'
b = Bear()
r = Rabbit()
o = Octothorpe()
print(b.eats())
print(r.eats())
print(o.eats())


#练习10：定义三个类：laser,claw,samrtphone,每个类都仅有一个方法does()，分别返回'disintegrate'(laser),
# 'crush'(claw),'ring'(smartphone).接着定义robot类，包含上述三个类的实例（对象）各一个，给robot定义does()方法用于
#输出它各部分的功能
class laser:
    def does(self):
        return 'disintegrate'
class claw:
    def does(self):
        return 'crush'
class smartphone:
    def does(self):
        return 'ring'
class robot:
    def __init__(self):
        self.laser = laser()
        self.claw = claw()
        self.smartphone = smartphone()
    def does(self):
        return '''I have many attachments:
        My laser,to %s.
        My claw,to %s.
        My samrtphone,to %s.''' % (
            self.laser.does(),
            self.claw.does(),
            self.smartphone.does())
robbie = robot()
print(robbie.does())