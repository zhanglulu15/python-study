#第六章对象和类

#使用class定义类
class person():
    def __init__(self,name):
        self.name = name
hunter = person('elmer fuud')
print('the mighty hunter:',hunter.name)   #在person内部，可以直接通过self.name访问name特性，而创建了一个实际对象后，需要通过hunter.name来访问

#继承
class car():
    def exclaim(self):
        print("I'm a car!")
class yugo(car):
    pass
give_me_a_car = car()   #为每个类创建对象
give_me_a_yugo = yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()  #没有进行任何操作，yugo自动从car那里继承了exclaim()方法


#覆盖方法
class car():
    def exclaim(self):
        print("Iim a car")
class yugo(car):
    def exclaim(self):
        print("I'm a yugo!much like a car,but not a car.")
give_me_a_car = car()   #为每个类创建一个对象
give_me_a_yugo = yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()


class person():
    def __init__(self,name):
        self.name = name
class MDPerson(person):
    def __init__(self,name):
        self.name = "Doctor" + name
class JDPerson(person):
    def __init__(self,name):
        self.name = "Esquire" + name
person = person('Fuud')
doctor = MDPerson('Fudd')
lawyer = JDPerson("Fudd")
print(person.name)
print(doctor.name)
print(lawyer.name)

#添加新的方法
class car():
    def exclaim(self):
        print("I'm a car")
class yugo(car):
    def exclaim(self):
        print("I,m a yugo!Mucg kike a car,but more yugo_ish")
    def need_a_push(self):
        print("A little help here")
give_me_a_car = car()
give_me_a_yugo = yugo()
give_me_a_yugo.need_a_push()  #yugo类的对象可以相应need_a_push()的方法,但是car不行


#使用super从父类得到帮助
class person():
    def __init__(self,name):
        self.name = name
class EmailPerson(person):
    def __init__(self,name,email):  #子类的__init__（）调用了父类的Person.__init__()方法，他会自动将self参数传递给父类
        super().__init__(name)   #通过super()方法获取了父类person的定义
        self.email = email
bob = EmailPerson('bob Fraples','bob@frapples.com')
print(bob.name)
print(bob.email)


#使用属性对特征进行访问和设置
class duck():
    def __init__(self,input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self,input_name):
        self.hidden_name = input_name
    name = property(get_name,set_name)  #第一个参数是getter方法，第二个是setter方法
fowl = duck('howard')
print(fowl.name)  #当尝试访问duck类对象的name特性时，get_name()会被自动调用

fowl.get_name()  #也可以显示调用get_name()，就像普通的getter方法一样

fowl.name = 'daffy'  #当对name特性执行赋值时，set_name()方法会被调用

print(fowl.name)

fowl.set_name('daffy')  #显示调用set_name()方法

#利用装饰器@property,指示getter方法
#利用name.setter,用于指示setter方法
class duck():
    def __init__(self,input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self,input_name):
        print('inside the setrer')
        self.hidden_name = input_name
fowl = duck('howard')
print(fowl.name)
fowl.name = 'donald'
print(fowl.name)


#鸭子类型
class quote():
    def __init__(self,person,words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def sys(self):
        return self.words + '.'
class questionquote(quote):
    def sys(self):
        return self.words + '?'
class exclamationquote(quote):
    def sys(self):
        return self.words + '!'
hunter = quote('elmer fudd',"I'm a hunting wabbits")
print(hunter.who(),'sys:',hunter.sys())

hunted1 = questionquote('bug bunny',"what's up,doc")
print(hunted1.who(),'sys:',hunted1.sys())

hunted2 = exclamationquote('daffy duck',"It's rabbit season")
print(hunted2.who(),'sys:',hunted2.sys())


