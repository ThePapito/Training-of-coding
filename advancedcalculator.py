print("Welcome,", end = " ")
print("In this program you will have to pick two numbers", end = " ")
print("and the operation")

a = int(input("1 number: "))
b = int(input("2 number: "))

def option1():
    print("Uruchomiono opcje nr1")
    print(a, "+", b, "=", a + b)
def option2():
    print("Uruchomiono opcje nr2")
    print(a, "-", b, "=", a - b)
def option3():
    print("Uruchomiono opcje nr3")
    print(a, "*", b, "=", a * b)
def option4():
    print("Uruchomiono opcje nr4")
    print(a, "/", b, "=", a / b)

print("1 - dodwanie ")
print("2 - odejmwoanie ")
print("3 - mnożenie ")
print("4 - dzielenie")
print("(Odpowiedż wybierasz wpisując numer odpowiadający działaniu)")

wybor = int(input("Jaka operacje wybierasz: "))

if wybor == 1:
    option1()
elif wybor == 2:
    option2()
elif wybor == 3:
    option3()
elif wybor == 4:
    option4()
else:
    print("Nie wybrales dzialania w odpowiedni sposob")