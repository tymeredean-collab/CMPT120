class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee:
  def __init__(self, name, idNumber, department):
    self.name = name
    self.idNumber = idNumber
    self.department = department
        
class Cake:
  def __init__(self, flavor, frosting):
    self.flavor = flavor
    self.frosting = frosting
  

class Cat:
  def __init__(self, name, age, fur_length):
    self.name = name
    self.age = age
    self.fur_length = fur_length
        
  def breedGuess(self):
    if self.fur_length == "long":
      return("Domestic Longhair")
    else:
      return("Domestic Shorthair")
            
class Car:
  def __init__(self, model, year, color):
    self.model = model
    self.year = year
    self.color = color

  def drive(self):
    return("The car is driving.")

class Laptop:
  def __init__(self, brand, storage):
    self.brand = brand
    self.storage = storage
  
        
def main():
    dog1 = Dog("Rocco" , 7)
    print(dog1.name, dog1.age)
    
    newEmployee = Employee("Eric", 10245, "IT")
    print(newEmployee.name)
    print(newEmployee.idNumber)
    print(newEmployee.department)
  
    newCake1 = Cake("Vanilla", "Strawberry")
    print(newCake1.flavor)
    print(newCake1.frosting)
    
    newCake2 = Cake("Chocolate", "Cream Cheese")
    print(newCake2.flavor)
    print(newCake2.frosting)
    
    cat1 = Cat("Tom", 5, "short")
    print(cat1.name)
    print(cat1.age)
    print(cat1.fur_length)
    
    cat2 = Cat("Jack", 8, "long")
    print(cat2.name)
    print(cat2.age)
    print(cat2.fur_length)

    print(cat1.breedGuess())
    
    car1 = Car("Toyota", 2024, "Red")
    print(car1.model, car1.year, car1.color)
    print(car1.drive())

main()
