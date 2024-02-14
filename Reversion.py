def reverse_integer(num):
    # Checking  if the number is negative
    if num < 0:
        sign = -1
        num = -num
    else:
        sign = 1

    # Reversing  the digits of the number
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10

    # Applying  the sign to the reversed number
    reversed_num *= sign
    return reversed_num

# Testing  the function
num = int(input("Enter an integer: "))
reversed_num = reverse_integer(num)
print("Reversed integer:", reversed_num)
