# fizzbuzz problem, prints
# multiples of 3 as fizz,
# multiples of 5 as buzz,
# multiples of 3 and 5 as fizzbuzz
for x in range(1, 101):
    # checks for multiples of 3 AND 5, uses modulo '%' to check if there is a remainder,
    # if not, data passes check, then executes print statement
    if x % 3 == 0 and x % 5 == 0:
        print('fizzbuzz')
    elif x % 3 == 0:
        print('fizz')
    elif x % 5 == 0:
        print('buzz')
    else:
        print(x)
