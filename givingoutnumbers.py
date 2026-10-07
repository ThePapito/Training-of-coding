print("Welcome")
a = int(input("Give me a number you want to start with: "))
n = int(input("How many more numbers would you like to see: "))
for x in range(a, a + n):
    if (a < a + n):
        print(a)
        a = a + 1 
print("Thats your answer.")