minVal = 1
while minVal <= 100:
    if minVal % 3 == 0 and minVal % 5 == 0:
        print("FizzBuzz")
    elif minVal % 3 == 0:
        print("Fizz")
    elif minVal % 5 == 0:
        print("Buzz")
    else:
        print(minVal)
    minVal += 1
