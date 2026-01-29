##Final Q1 ##

print("Menu\n ---------------\nOption 1: Joke\nOption 2: Food\nOption 3: Numbers\n---------------")

print("Hello")

option = float(input("Enter a number to choose an option: "))

if (option == 1):
    name = input("Enter your name: ")
    print("Why was ", name, " so bad at soccer?")
    print(name, "kept running away from the ball.")
elif(option == 2):
    food = input("Enter your favorite food: ")
    for i in range(20):
        print(food)
elif(option == 3):
    x = 1
    while (x != 0):
        x = float(input("Enter a number: "))
        print("WARNING: Program will continue until 0 is entered.")

