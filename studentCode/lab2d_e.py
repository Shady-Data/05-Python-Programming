# **Lab 2D: Strings**

# **Instructions:**

# Write a program that reverses a user inputted string then outputs the new string, in all uppercase letters.

# **Bonus:** Add additional functionality, experiment with other string methods.

def string_manip():
    user_string = input("2d. Enter a string to mess around with:\n")
    out_string = user_string.upper()[::-1]
    return out_string

print(string_manip())

# ## Lab 2E: Count Words

# **Instructions:**

# Write a program that takes a string as user input then counts the number of words in that sentence.

# **Bonus:** Add additional functionality, experiment with other string methods.

# ex: Output number of characters, number of uppercase letters, etc...

def word_counter():
    user_string = input("2e. Enter a string:\n")
    word_count = len(user_string.split(' '))
    char_count = len(user_string)
    upper_count = 0
    lower_count = 0
    digit_count = 0

    for char in user_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            digit_count += 1
    
    print("# of words: %d"% word_count)
    print("# of characters: %d"% char_count)
    print("# of uppercase letters: %d"% upper_count)
    print("# of lowercase letters: %d"% lower_count)
    print("# of digits/numbers: %d"% digit_count)

word_counter()