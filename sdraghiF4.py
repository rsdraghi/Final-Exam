## Final q4 ##

def nothing(number):
    for i in range(number):
        print("Happy New Year!")
    return

number = int(input("Enter a number between 1 and 10: "))

if (number > 0 and number < 11): 
    nothing(number)
elif(number < 1 or number > 10): 
    print("Program failed. Run again and enter a number between 1 and 10.")
