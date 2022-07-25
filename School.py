class Student:
    def __init__(self,name,age,gender,cls):
        self.name = name
        self.cls = cls
        self.age = age
        self.gender = gender

    def __str__(self):
        return "{},{},{},{}".format(self.name,self.age,self.gender,self.cls)