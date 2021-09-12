# if statement = a block of code that will execute if it's condition is true

age = int(input("How old are you? : "))

# we always begin with an if statement 
if age == 100:
    print("You are centure old")
elif age >= 18:
    print("You are an adult!")
#elif age == 100:
#    print("You are centure old") # certainly the program will print "You are an adult!" 
                                 #that because we first check if statement so we have to move this statement to beginning from program
elif age < 0:
    print("You haven't been born yet")
else:
    print("You are a child!")