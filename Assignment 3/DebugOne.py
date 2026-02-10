
def main():

  ## that's not right... how can we make sure it also includes equals 5?
    temp = 5
    if temp >= 5:
        print("temp is greater than or equal to 5")
        
    
  #enter your name here
  ##  '''in this if/elif/else, add 4 misspellings of your name for if/elif comparisons, and then have your last elif be elif name = "your properly spelled name"
    name = "Ty"
  
    if name == "Tye":
        print("That's not right!")
    elif name == "Tie":
        print("That's not right!")
    elif name == "Tai":
        print("That's not right!")
    elif name == "Tey":
        print("That's not right!")
    elif name == "Ty":
        print("You're correct!")
      
  

    
    
    #we're gonna check if a user input number is even
    #pick any number
    even = input(int("Enter a number to find out if its even or odd"))
    even = int(even)
    #what do we replace the question marks with?
    if even % 2 == 0:
        #what would be appropriate in these print statements?
        print("Even")
    else:
        print("Odd")
  
  
    #i'm trying to do math with the numbers 2 and 4, but it's getting 3 and 5... why?
    numbers = [1,2,3,4,5]
    print(numbers[1])
    print(numbers[3])
    print(numbers[3] / numbers[1])
    print(numbers[3] * numbers[1])
    
    #again, why is it getting 7 and 20, I wanted 3 and 29!
    numbers2 = [465,3,30,7,29,20,82,13,5]
    print(numbers2[1])
    print(numbers2[4])
    
main()
    
