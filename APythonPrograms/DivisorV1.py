# program that asks user for number and prints all divisors of user inputted number.
user_num = int(input("Give me a random number and I'll tell you all the divisors for that number "))
# num represents numbers between 1 and 100
for num in range(1, 101):
    # if num % 'modulo' user_num is 0 then that num is a divisor of user_num
    if num % user_num == 0:
        print(num, "is a divisor of ", user_num)
