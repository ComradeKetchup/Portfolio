# asks user for number between 1 and 1000, checks if input is odd or even then lets user know whether it is or is not

# while loop to keep program looping
while True:
    # asks user for value between 1 and 1000
    user_input = input("Enter a number between 1 and 1000: ")
    # ensures user input is an int
    user_input.isdigit()
    # converts user input into an int
    user_input = int(user_input)

# if loop parses user input within specified range
    if user_input in range(1, 1001):
        # checks if number is divisible by 2, if no remainder than number is even
        if user_input % 2 == 0:
            print(user_input, "this number is even!")
        # if user input is not even, then it is odd
        else:
            print(user_input, "this number is odd!")
    # asks user for another number
    print("How about another number?")
