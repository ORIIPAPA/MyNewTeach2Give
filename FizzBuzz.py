# Inserting the range
for num in range(1, 101):
    # generating FizzBuzz if numbers are divisible by both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        # generate Fizz when divisible by only 3
    elif num % 3 == 0:
        print("Fizz")
    # generate Buzz if divisible by only 5
    elif num % 5 == 0:
        print("Buzz")
        # generate the number if the two conditions does not hold both
    else:
        print(num)
