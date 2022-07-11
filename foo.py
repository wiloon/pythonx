print("Hello, World!")
name = "hello world"
print(name.title())
print(name.upper())
print(name.lower())
print("\tpython\nfoo")

# abc
print("foo")

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
print(magician)

for value in range(1, 5):
    print(value)

import sys
from netaddr import IPNetwork
from path0.foo import fun0

# print
msg = "hello world"
print(msg)


# class
class Student0(object):
    pass


foo = Student0()

foo.field0 = "value0"

print(foo)
print(foo.field0)


# class func
class Student1(object):
    # 相当于构造函数
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    # 类内部访问数据的函数
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bar = Student1("name0", 60)

print(bar)
print(bar.name)


def print_score(std):
    print('%s: %s' % (std.name, std.score))


print_score(bar)

bar.print_score()

print(bar.get_grade())
fun0()


# underscore
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 42


# dict
dict0 = {'key0': 'value0', 'key1': 'value1', 'key2': 'value2'}

print(dict0)

dict0 = {'key0': 'value00', 'key2': 'value2'}
print(dict0)

dict0.update({'key0': 'value000'})
dict0.update({'key3': 'value3'})
print(dict0)

# exception
def func1():
    raise Exception("--func1 exception--")


def exception0():
    try:
        func1()
    except Exception as e:
        print("exception...")
        print(e)


exception0()


# traceback
def func2():
    raise Exception("--func2 exception--")


def exception1():
    import traceback
    try:
        func2()
    except Exception as e:
        exc_type, exc_value, exc_traceback_obj = sys.exc_info()
        traceback.print_tb(exc_traceback_obj)


exception1()

# list
list0 = ['str']
print(list0)

print("------")

ip_network = IPNetwork('192.168.1.1')  # 默认掩码255.255.255.255或者是32
print(ip_network)  # __str__方法返回的是字符串表达形式 cidr的表达方式
print(repr(ip_network))  # __repr__方法是类名称内包裹cidr的表达方式

ip_network = IPNetwork('192.1.0.29/25')
print(ip_network)  # __str__方法返回的是字符串表达形式 cidr的表达方式
print(repr(ip_network))  # __repr__方法是类名称内包裹cidr的表达方式

# IP v4 network with netmask
ip_network = IPNetwork('192.168.1.0/255.255.255.0')

print(ip_network)  # __str__方法返回的是字符串表达形式 cidr的表达方式
print(repr(ip_network))  # __repr__方法是类名称内包裹cidr的表达方式
print("------")
# IP v4 network with cidr prefix netmask
ip_network = IPNetwork('192.1.0.29/25')
print("print:")
print(ip_network)  # __str__方法返回的是字符串表达形式 cidr的表达方式
print("ip_network:")
print(repr(ip_network))  # __repr__方法是类名称内包裹cidr的表达方式
print("ip_network.network:")
print(repr(ip_network.network))  # 192.1.0.0, 网络位，会根据IP地址和掩码计算出网络位
print("ip_network.broadcast:")
print(repr(ip_network.broadcast))  # 192.1.0.127
print(repr(ip_network.netmask))  # 返回一个掩码是IPAdress类，如果想用字符串，必须强制转str，或者是所在的函数比如format会自动调用__str__方法
print(repr(ip_network.prefixlen), type(repr(ip_network.prefixlen)))  # 返回的掩码的字符串
print(repr(ip_network.ip))  # 返回的是我们传入的主机位
print("ip_network[1]:")
print(repr(ip_network[1]))
print("ip_network[-2]:")
print(repr(ip_network[-2]))
print("------")
for num in range(0, 20):  # 迭代 10 到 20 之间的数字
    print(repr(ip_network[num]))
print("------")
for num in range(-10, 10):  # 迭代 10 到 20 之间的数字
    print(num)
    print(repr(ip_network[num]))
