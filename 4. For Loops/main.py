import time
# for loop = a stetement that will execute it's block of code
#            a limited amount of times
# so what's the differences between for loop and while loop?
#       while loop  = unlimited    (while loop could iterate an unlimited or infinite amount of times depending on the condition)
#       for loop    = limited      (for loop will only iterate a limited amount of times)

#for index in range(10):
#    print(index) # so the counting will be begin with zero because computer always start with zero or index number always begin with zero.
# how the way to counting index begin with one?
'''for index in range(10):
    print(index+1)''' # You have to add 1 after index so that the counting will begin with 1

# let's count a range between two number 
'''for index in range (50,100): # so within my range function will pass two numbers 
    print(index)'''          # the first number (50) will be the starting point, the first number is inclusive
                             # the second number (100) is the ending point, the second number is exclusive
# if you wanted to include last number since it's exclusive what we could do is just add one to the end
# like this : 
'''for index in range (50,100+1):
    print(index)'''

# you can add third argument and this will fucntion as the step how much you want to count up or down by
#so this time lets count up by two / di loncatin 2 kali
'''for index in range (50,100+1,2): # add comma two we're passing in a third argument this time, so the program will count up by two 
    print(index)'''

# we can use string in loops
# like this:
'''for index in ("Ice Bear"):
    print(index)''' # Ice Bear will be printed in Newline :)

# we can make a timer 
for seconds in range (10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!!!")