
# user_play = input("Would you like to play a game? ")

while True:
    user_palindrome = input("Enter a word to check if it is a palindrome ")

    if user_palindrome[::-1] == user_palindrome:
        print("The word, ", user_palindrome, " was a palindrome!")
    else:
        print("That word was not a palindrome, sorry!")
