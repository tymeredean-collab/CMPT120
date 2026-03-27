import random
def bust(num1, num2, num3):
  total = num1 + num2 + num3
  if total <= 21:
    return(total)
  elif num1 == 11 or num2 == 11 or num3 == 11:
    return total - 10
  else:
        return(0)






def main():
  val1 = random.randint(1, 11)
  val2 = random.randint(1, 11)
  val3 = random.randint(1, 11)
 
  print("Values:", val1, val2, val3)
  print("Result:", bust(val1, val2, val3))



main()


# I learned how to use random.randint() to generate numbers between 1 and 11, and different conditions, and return the correct value.
