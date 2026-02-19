def main():
  Numbers = [12, 44, 33, 22, 39, 28, 18, 9]
  for i in range (len(Numbers)):
    if Numbers[i] > 35:
      print("Index", i, "Greater than 35")
    elif 20 <= Numbers[i] <= 35:
      print("Index", i, "Between 20 and 35")
    elif 5 <= Numbers[i] <= 20:
      print("Index", i, "Between 5 and 20")
    else:
      print("Index", i, "Number is less than 5")

main()


## What I learned from this assignment was to use an if/else/ifelse statement to check each index to correctly apply it towards the right condition using a loop.

 
  
  
