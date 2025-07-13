# Prompt the user to input their current age
# input() gets text from the user and we store it in a variable.
current_age_str = input("How old are you? ")

# Convert the string input to an integer to do math
# int() turns the text (string) into a whole number (integer).
current_age = int(current_age_str)

# Calculate the age in 2050 (which is 27 years from 2023)
future_age = current_age + 27

# Print the final result
print(f"In 2050, you will be {future_age} years old.")