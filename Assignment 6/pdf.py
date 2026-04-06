import random
class Student:
  def __init__(self, name, studentID, year, major, gpa):
    self.name = name
    self.studentID = studentID
    self.year = year
    self.major = major
    self.gpa = gpa
  
  
  def honors_program(self):
    if self.gpa > 3.5:
      return True
    else:
      return False
 
  
  def free_lunch(self):
    random_id = random.randint(10000, 99999)
    if self.studentID == random_id:
      print("Winner!", self.name, " gets free lunch")
    else:
      print("Loser")



  


def main():
  student1 = Student("Tymere", 23876, "Senior", "Information Technology", 3.3)
  print(student1.honors_program())
  print(student1.free_lunch())
  student2 = Student("Andy", 34123, "Sophomore", "Computer Science", 2.4)
  print(student2.honors_program())
  print(student2.free_lunch())
  student3 = Student("Jackson", 47932, "Junior", "Philosophy", 3.9)
  print(student3.honors_program())
  print(student3.free_lunch())




main()

##The biggest takeaway from this assignment was learning how to build classes and use functions to make objects perform specific tasks
