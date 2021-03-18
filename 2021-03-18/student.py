from person import Person

class Student(Person):
 def __init__(self, studentName, studentAge, studentId):
 #izsauc baazes klases konstruktoru, lai inicializetu
 # baazes klases datu elementus
  Person.__init__(self, studentName, studentAge)
  self.id = studentId

 def get_id(self):
     return self.id

 def __str__(self):
     return(f'{self.name}, {self.age}, {self.id}')