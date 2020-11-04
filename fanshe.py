class Person():
    def __init__(self, age):
        self.age = age

    def play(self, name,age):
        print(f'{name}今年{age}喜欢玩耍')


def add(x):
    return x+1

person = Person(20)
print(getattr(person, 'age'))
print(getattr(person, 'play'))
#getattr(person, 'play') 函数 跟正常函数的用法一样
getattr(person, 'play')('xiaoming',80)
# hasattr()可以判断某个对象是否有某个属性或者方法 布尔类型 返回  True
# False
print(hasattr(person, 'age'))
print(hasattr(person, 'add'))
# setattr(对象，实例方法/属性,函数名字/具体的值)
setattr(person,'add_method',add)
print(person.add_method(100))
setattr(person,'gender','男')
print(person.gender)

