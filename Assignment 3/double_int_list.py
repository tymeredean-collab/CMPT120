def main():

  doubleValue = 6.8
  
  intValue = 16
  
  print(doubleValue + intValue)
  print(doubleValue - intValue)
  print(doubleValue * intValue)
  print(doubleValue / intValue)
  
  
  
  myFriends = ["Joe", "Phil", "Tyler", "Tim", "Henry"]
  print(myFriends[2])
  print(myFriends[3])
  
  fiveNumbers = [3, 4, 5, 97, 23]
  print(fiveNumbers[2] + fiveNumbers[4])
  print(fiveNumbers[1] - fiveNumbers[0])
  print(fiveNumbers[3] * fiveNumbers[4])
  print(fiveNumbers[2] / fiveNumbers[4])
  fiveNumbers[3] = 22
  fiveNumbers[2] = 12
  print(fiveNumbers)
  
  petName = input("What is your pet's name: ")
  myPets = ["Dog", "Frog", "Fish", "Hamster"]
  myPets.append(petName)
  print(myPets)

main()
  
