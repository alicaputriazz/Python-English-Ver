# Nested Loops =    The "inner loop" will finish all of it's iterations before
#                   finishing one iteration of the "outer loop"

rows = int(input("How many rows? : ")) # the outer for loops will be in charge of the rows 
columns = int(input("How many columns? : ")) # the inner for loops will be in charge of the columns 
symbol = input("Enter a symbol to use: ")

for i in range(rows): # create an outer for loops
    for j in range(columns): # j is to wrtie for inner loops as an index 
        print(symbol, end="")
    print()