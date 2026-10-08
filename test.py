print("Welcome")

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

    
