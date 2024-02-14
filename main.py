def count_vowels(Letters):
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    # Initialize a counter for vowels
    vowel_count = 0

    # Iterating  through each character in the sentence
    for char in Letters:
        # Checking  if the character is a vowel
        if char in vowels:
            vowel_count += 1

    return vowel_count


# Testing  the function
sentence = input("Enter a sentence: ")
num_vowels = count_vowels(sentence)
print("Number of vowels in the sentence:", num_vowels)
