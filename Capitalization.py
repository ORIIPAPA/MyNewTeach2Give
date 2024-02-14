def capitalize_words(My_String):
    # Split the input string into words
    words = My_String.split()

    # Capitalize the first letter of each word
    capitalized_words = [word.capitalize() for word in words]

    # Join the capitalized words back into a string
    new_string = ' '.join(capitalized_words)

    return new_string


# Test the function
input_string = input("Enter a string: ")
result = capitalize_words(input_string)
print("Capitalized words are therefore:", result)
