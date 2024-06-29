class Person:
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Person.count=Person.count+1
    def get_name(self):
        print('name is %s' % self.name)
    def get_age(self):
        print('age is %s' % self.age)
    def get_info(self):
        print('name is %s and age is %i' % (self.name, self.age))
    def return_count(self):
        return (Person.count)
jadi=Person('jadi',40)
mahmoud=Person('mahmoud',31)
jadi.get_name()
jadi.get_info()
jadi.get_age()
print('at the moment I have %i persons' % jadi.return_count())
print('-----------------------------------------------')