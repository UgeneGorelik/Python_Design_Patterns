#Observer Design Pattern

import abc


#class that contains Observers that monitors its state
class HowToObserve:
    def __init__(self):
        self.observers=[]
        self._subject_state = None

    def attachObserver(self,o):
        self.observers.append(o)

    def _LetAllKnow(self):
        for x in self.observers:
            x.update(self._subject_state)

    @property
    def subject_state(self):
        return self._subject_state

    @subject_state.setter
    def subject_state(self, arg):
        self._subject_state = arg
        self._LetAllKnow()

#abstract Observer Object
class ObserverAbstract(metaclass=abc.ABCMeta):
    def __init__(self):
        self.state=None

    def update(self,item):
        self.state=item
        self.DisplayTheChanges()

    def DisplayTheChanges(self):
        pass

#Actual Observer Objects
class ActualObserver1(ObserverAbstract):
     def DisplayTheChanges(self):
         print("ActualObserver1 Reports "+ self.state )




class ActualObserver2(ObserverAbstract):
     def DisplayTheChanges(self):
         print("ActualObserver2 Reports "+ self.state )


if __name__=="__main__":
    a1=ActualObserver1()
    a2=ActualObserver2()
    h=HowToObserve()
    h.attachObserver(a1)
    h.attachObserver(a2)
    h._subject_state="updated state"
    h._LetAllKnow()