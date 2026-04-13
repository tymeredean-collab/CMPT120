

class Animal:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        

class Dog(Animal):
    def __init__(self, age, name, breed):
        super().__init__(age, name)
        self.breed = breed


  
    def fav_breed(self):
      if self.breed == "boston terrier":
        return ("Ty's fav breed")
      else:
        return("it's still a good dawg")
                
    
   

class Cat(Animal):
    def __init__(self, age, name, has_ear_clip):
      super().__init__(age, name)
      self.has_ear_clip = has_ear_clip


  
    def check_clip(self):
      if self.has_ear_clip == True:
        return "This cat must have been a stray at some point."
      else:
        return "This cat was likely always an inside cat."
      
      
      
        
        
def main():
    a1 = Animal(10, "buddy")
    print(a1.name)
    d1 = Dog(10, "frank", "lab")
    print(d1.breed)
    print(d1.fav_breed())
    c1 = Cat(10, "Toby", True)
    print(c1.check_clip())


main()
