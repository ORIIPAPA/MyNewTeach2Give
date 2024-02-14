# Function to generate Fibonacci sequence
def produce_fibonacci(limit):
    # Initializing  variables for the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Generating Fibonacci numbers until the limit
    while True:
        # Calculation of  the next Fibonacci number
        next_num = fib_sequence[-1] + fib_sequence[-2]

        # Breaking  the loop if the next Fibonacci number exceeds the limit
        if next_num > limit:
            break

        # Append the next Fibonacci number to the sequence
        fib_sequence.append(next_num)

    return fib_sequence


# Generate Fibonacci sequence up to 100
fibonacci_sequence = produce_fibonacci(100)

# Print the Fibonacci sequence
print("The Fibonacci Sequence up to 100 are:")
print(fibonacci_sequence)
