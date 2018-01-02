#Factory Design Pattern


#class that have the Function to create new classes
#like Factory creates Products on demand
class FactoryItself(object):
    makes = ""

    @staticmethod
    def getProduct(item):
        if item=="toy":
            return toy()
        if item=="gun":
            return gun()

#classes that can be created by the factory
class toy(FactoryItself):
    makes = "toy"


class gun(FactoryItself):
    makes = "gun"

FactoryItself.getProduct("toy")