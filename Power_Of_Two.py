def power_of_two(n):
    # Checking  if n is positive
    if n <= 0:
        return False
    # Checking  if n is a power of two
    return (n & (n - 1)) == 0


# Testing my   function
num = int(input("Enter an integer value: "))
result = power_of_two(num)
if result:
    print(num, "True")
else:
    print(num, "False")
