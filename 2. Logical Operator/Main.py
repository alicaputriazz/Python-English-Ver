# Logical operator (and.or) = used to check if two or more conditional statement are true.

temp = int(input("what is the temperature outside? : "))

if temp >= 0 and temp <= 30: #with the and logical operator in order for this condition to be true / both condition must be true 
    print("the temperature is very good today!")
    print("go outside!")
elif temp < 0 or temp > 30: # with the or logical operator as long as one of these condition are true then the entire statement is true it doesnt matter if one of them is false 
    print("the temperature is bad today")
    print("please stay inside")