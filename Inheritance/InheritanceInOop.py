class Computer:
    counter=0
    def __init__(self,ram,hard,cpu):
        Computer.counter+=1
        self.ram=ram
        self.hard=hard
        self.cpu=cpu
    def __del__(self):
        Computer.counter-=1
    
    def value(self):
        return self.ram+self.hard+self.cpu
class Laptop(Computer):
    def value(self):
        return self.ram+self.hard+self.cpu+self.size

pc1=Computer(12,2,4)
print(pc1.value())
del pc1

laptop1=Laptop(16,2,4)
laptop1.size=13
print(laptop1.value())