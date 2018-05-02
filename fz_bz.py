
fzbz_num = int(input("Please input a number: "))

if (fzbz_num % 3 == 0 and fzbz_num % 5 == 0):
    print("Fizz Buzz")
elif (fzbz_num % 5 == 0):
    print("Buzz")
elif (fzbz_num % 3 == 0):
    print("Fizz")
