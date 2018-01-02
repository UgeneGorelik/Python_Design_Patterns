#startegy Design Pattern

import  abc

#class that can recieve the strategy it can implement and run the strategy
class ClassThatChoosesStartegy:
    def __init__(self,st):
        self.strategy=st

    def set_startegy(self,st):
        self.strategy=st

    def ExecuteStrategy(self):
        self.strategy.doStuff()

#the Abstarct Strategy Class
class StrategyAbstarct(metaclass=abc.ABCMeta):
     def __init__(self,name):
         self.Myname=name

     def doStuff(self):
         pass

#the Strategies impelmented
class actualStrategy1(StrategyAbstarct):
    def doStuff(self):
        print("i am actualStrategy1 and my name is "+self.Myname)

class actualStrategy2(StrategyAbstarct):
    def doStuff(self):
        print("i am actualStrategy2 and my name is "+self.Myname)

if __name__=="__main__":
    a=actualStrategy1("s1")

    c=ClassThatChoosesStartegy(a)

    c.ExecuteStrategy()
