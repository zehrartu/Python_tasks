for num in range(1, 101):
    if num % 5 == 0 and num % 7 == 0:
        print("FizzBuzz", end=", ")
    elif num % 5 == 0:
        print("Fizz", end=", ")
    elif num % 7 == 0:
        print("Buzz", end=", ")
    else:
        print(num, end=", ")
