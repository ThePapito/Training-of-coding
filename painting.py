def line():

    a = int(input("How long should the line be: "))
    b = 0

    while b < a:
        print("o", end = "")
        b += 1

def triangle():

    a = int(input("How tall should the traignle be:"))
    b = 0 
    x = 0

    while b < a:

        if x < a:
            print("o", end = "")
            x += 1
        else:
            x = 0
            a -= 1
            print()

def square():
    a = int(input("How tall should the square be:"))
    b = int(input("How wide should the square be:")) 
    x = 0
    y = 0

    while y < a:
        
        if x < b:
            print("o", end = "")
            x += 1
        else:
            print()
            x = 0
            y += 1
        
        

print("Welcome")
print("In this code you will be able to draw diffrent thigs", end = " ")
print("You can choose from:")
print("1. line")
print("2. triangle")
print("3. Square")

z = int(input("To choose you have to write the proper number: "))

if z == 1:
    line()
elif z == 2:
    triangle()
elif z == 3:
    square()
else:
    print("You have chosen the wrong way. Im sorry...")
