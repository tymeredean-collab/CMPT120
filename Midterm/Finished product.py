## Athlete Builder Simulator 
def main():
  player_name = input("What is your name: ")
  print("Hello", player_name, "Welcome to the Athlete Builder Simulator")
 ##Our starting attributes for the player
  strength = 60
  speed = 75
  shooting = 65
  stamina = 70
  week = 1
  
  overall = (strength + speed + shooting + stamina)//4 

  while overall < 90 and stamina > 0:   ## while loop conditioning 
    print("Week: ", week)
    print("Strength: ", strength)
    print("Speed: ", speed)
    print("Shooting: ", shooting)
    print("Stamina: ", stamina)
    print("1. Lift (increase strength)")
    print("2. Sprint (increase speed)")
    print("3. Shoot (increase shooting)")
    print("4. Recover (increase stamina)")
    
    user_choice = int(input("Pick a number: ")) ##This checks the user's input and applies their choice to their player
    
    if user_choice == 1:
      strength += 3
      stamina -= 2
    elif user_choice == 2:
      speed += 3
      stamina -= 2
    elif user_choice == 3:
      shooting += 3
      stamina -= 2
    elif user_choice == 4:
      stamina += 5
    else:
      print("invalid choice")
    week = week + 1
    overall = (strength + speed + shooting + stamina)//4 ## recalculates the overall based off the user's choice
    print("Overall: " , overall)
    
    if overall >= 90:
      print("Congratualations, you are an elite athlete")
    elif stamina <= 0:
      print("Burned out!")
  main()
