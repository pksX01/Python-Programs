class Animal(object):
    def __init__(self):
        pass
    def message(self):
        print ("I am an animal")

class Lion(Animal):
    def __init__(self):
        super(Lion, self).__init__()
    def message(self):
        print ("I am a lion")
        super(Lion, self).message()

lionObj = Lion()
lionObj.message()
