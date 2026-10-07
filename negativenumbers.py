print("Give me any number:")
a = int(input())
while a >= 0 :
    print("This number is positive. Please type in another one:")
    a = int(input())
    if a < 0:
        print("This number is negative.")
        
