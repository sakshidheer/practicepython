from datetime import date
from datetime import timedelta

class Student():
    def __init__(self,id, name, day, month, year):
        self.id = id
        self.name = name
        self.day = day
        self.month = month
        self.year = year
    
    def get_age(self):
        birthday = date(self.year, self.month, self.day)
        today = date.today()
        diff = today - birthday
        return diff.days//365
        
        