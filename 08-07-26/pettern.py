#basic patterns in python

#1. patterns (without space pattern)

size = 10

for i in range(size):
    for j in range(size):
        print("*" , end="")
    print()

#2.right-angled triangle pattern

size = int(input("Enter your size : "))

for i in range(1 , size + 1):
    for j in range(i):
        print(" * " , end="")
    print()

#3.inverted right-angled triangle patterns

size = 10

for i in range(size , 0 , -1):
    for j in range(i):
        print(' * ' , end="")
    print()
    
#4. patterns (with space)

#pyramid pattern

rows = 5

for i in range(1 , rows + 1):
    for j in range(rows - i):
        print("  " , end="")
    for k in range(2 * i - 1):
        print("*" , end="")
    print()


for i in range(rows - 1 , 0 , -1):
    for j in range(rows - i):
        print("  " , end="")
    for k in range(2 * i - 1):
        print("*" , end="")
    print()

# Diamond Patterns

rows = 5  # You can change this to any number

# Upper half of the diamond (including the middle row)
for i in range(1, rows + 1):
    # Print leading spaces
    print("  " * (rows - i), end="")
    
    # Print the stars and inner blanks
    if i == 1:
        print("*")
    else:
        print("*" + "  " * (2 * i - 3) + "*")

# Lower half of the diamond
for i in range(rows - 1, 0, -1):
    # Print leading spaces
    print("  " * (rows - i), end="")
    
    # Print the stars and inner blanks
    if i == 1:
        print("*")
    else:
        print("*" + "  " * (2 * i - 3) + "*")






