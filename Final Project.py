class Student:
  def __init__(self, name, year, major, cwid, gpa):
    self.name = name
    self.year = year
    self.major = major
    self.cwid = cwid
    self.gpa = gpa


def main():
  s1 = Student("Tymere", 2026, "Information Technology", 20134020, 3.1)
  s2 = Student("Jack", 2028, "Communications", 13902121, 2.9)
  s3 = Student("Tom", 2027, "Philosophy", 20137831, 2.5)
  s4 = Student("Anderson", 2029, "Art", 45924500, 3.5)
  s5 = Student("Elijah", 2026, "Criminal Justice", 98821499, 3.0)
  
  student_list = [s1, s2, s3, s4, s5]
  name = input("Please enter your name: ")
  year = int(input("Please enter your year: "))
  major = input("Please enter your major: ")
  cwid = int(input("Please enter your cwid: "))
  gpa = float(input("Please enter your gpa: "))
  print()
  
  if gpa < 0:
    print("Invalid GPA")
  elif cwid < 10000000 or cwid > 99999999:
    print("Invalid CWID")
  else:
    new_student = Student(name, year, major, cwid, gpa)
    student_list.append(new_student)
  
  for student in student_list:
    print("Name:", student.name)
    print("Year:", student.year)
    print("Major:", student.major)
    print("CWID:", student.cwid)
    print("GPA:", student.gpa)
    print()
  
  
  file = open("students.txt", "w")
  for student in student_list:
    file.write(student.name + ", " + str(student.year) + ", " + student.major + ", " + str(student.cwid) + ", " + str(student.gpa) + "\n")
  
  file.close()
  seniors_count(student_list)

def seniors_count(student_list):
  count = 0
  
  for student in student_list:
    if student.year == 2026:
      count = count + 1
  
  print("The total number of seniors is:", count)

main()



