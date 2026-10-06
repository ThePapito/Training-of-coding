print("Welcome to an easy calculator.")
print("I would love you to pick two numbers separetly", end=" ")
print("and select the right operation from +, -, *, /.")
print("So lets start.")
x = int(input("First number: "))
y = int(input("Second number: "))
z = input("The operation of your choice would be: ")
a = "+"
b = "-"
c = "*"
d = "/"
print("This is your solution:", end=" ")
if z == a:
    print(x,z,y ,"=", (x+y))
if z == b:
    print(x,z,y ,"=", (x-y))
if z == c:
    print(x,z,y ,"=", (x*y))
if z == d:
    print(x,z,y ,"=", (x/y))
