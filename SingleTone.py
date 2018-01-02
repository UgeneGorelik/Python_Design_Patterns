#SingleTone Design Patterns it should have only one Class created
#OtherWise Throws Exception


class SingleTone:
    single=None
    def __init__(self):
        if SingleTone.single:
            raise SingleTone.single
        else:
            SingleTone.single=self



s=SingleTone()

#Here We wil see the exception
s=SingleTone()
