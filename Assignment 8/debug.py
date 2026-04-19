class Device:
    def __init__(self, brand, battery):
      self.brand = brand
      self.battery = battery
      self.powered_on = False
    
    def power_on(self):
      if self.powered_on == False:
        print(f"{self.brand} is powering on")
        self.powered_on = True
      else:
        print(f"{self.brand} is already on")
  

    def info(self):
      print(f"Brand: {self.brand}, Battery Life: {self.battery}")
     

class Phone(Device):
    def __init__(self, brand, battery, carrier):
      super().__init__(brand, battery)
      self.carrier = carrier
      
    
    def call(self):
      print(f"i am calling using {self.carrier}")
   
    

class Laptop(Device):
    def __init__(self, brand, battery, ram):
      super().__init__(brand, battery)
      self.ram = ram
   
    
    def ramCheck(self):
      if self.ram > 4:
        return ("they're all set")
      else:
        return ("Upgrade time baby!")
    




def main():
  D1 = Device("iPhone", 65)
  D1.power_on()
  D1.info()
 
  P1 = Phone("iPhone", 45, "Verizon")
  P1.call()
  P1.power_on()
  P1.info()
  
  L1 = Laptop("Macbook", 57, 3)
  L1.info()
  L1.power_on()
  print(L1.ramCheck())

#Create a generic device, phone, and laptop
#use all their functions

main()
