class Person:
 #konstruktors
     def __init__(self, personName, personAge):
         self.name = personName
         self.age = personAge

 #metodes
     def get_name (self):
         return self.name

     def get_age(self):
         return self.age

     def __str__(self):
         return(f'{self.name}, {self.age}')
     
     def print_info(self):
         print(f'name: {self.name}, age: {self.age}')
