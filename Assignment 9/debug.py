#take the names from the text file
#Write a short introduction for each person
#"Hi my name is (name) and I (make up a fun fact i dont care, the more insane the better)

#add your name to the text file using code :)

def main():
  file = "hw.txt"
  f = open(file, "a")
  f.write("Ty")
  f.close()
  
  f = open(file, "r")
  names = f.readlines()
  f.close()

  for name in names:
        name = name.strip()
        print(f"Hi my name is {name} and I once fought a bear over a parking spot.")


main()
  
