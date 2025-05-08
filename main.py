
# Write a function check_blood_pressure which reads the systolic and diastolic blood pressure value in mmHg as an integer from the console. The function has no arguments.
# The WHO category for the blood pressure is then determined and returned as a string from the function.
# The following classification applies:
# Category	            Systolic (mmHg)	    Diastolic (mmHg)	WHO Classification
# Normal	                < 120	            < 80	            Normal
# Elevated	                120–129	            < 80	            Elevated
# Stage 1 Hypertension	    130–139	            80–89	            Hypertension stage 1
# Stage 2 Hypertension	    ≥ 140	            ≥ 90	            Hypertension stage 2
# Hypertensive Crisis	    > 180	            > 120	            Hypertensive Crisis - Immediate medical attention needed
#
# If input is a negative number program should return "Invalid input"
# Attention: If the two values result in different categories, the higher category counts as the overall assessment!

def check_blood_pressure():
    sys = int(input('Please enter Systolic value: '))
    dia = int(input('Please enter Diastolic value: '))
    if sys < 0 or dia < 0:
        return "Invalid input"
    if sys > 180 or dia > 120:
        return "Hypertensive Crisis - Immediate medical attention needed"
    elif sys >= 140 or dia >= 90:
        return "Stage 2 Hypertension"
    elif (130 <= sys <= 139) or (80 <= dia <= 89):
        return "Stage 1 Hypertension"
    elif (120 <= sys <= 129) and dia < 80:
        return "Elevated"
    elif sys < 120 and dia < 80:
        return "Normal"
    return None


# Write a magicSquareMatrix function to which two parameters are passed.
# Firstly, a number that defines the size of the matrix and secondly, a letter between ‘A’ and ‘Z’ (upper case).
# Check whether the number is between 1 and 42 (inclusive).
# If given size and symbol are invalid the function returns "Invalid number and invalid symbol"
# If only size is invalid the function returns "Invalid number", if only the symbol is negative the function returns "Invalid symbol"
# If both values are valid, create a matrix with letters in ascending order from the starting letter in matrix form.
# When you reach the letter 'Z', start counting again from 'A'.
# The matrix is returned from the function.

# Hint: use ord() function to get a numerical value from a one-character string.
# e.g.:
#   letter = 'A'
#   number = ord(letter)
# You can then increase the numerical value and cast to character again, to get the next letter:
#   next = chr(number + 1) # will print 'B'
# see running example below

# Constants
CHAR_A = 65
CHAR_Z = 90

def increase_letter_number(ln):
    if ln >= 90:
        return 65
    else:
        return ln + 1

def magic_square(size: int, letter: str):
    letter_number = ord(letter)
    if (size <= 0 or size > 42) and (letter_number < CHAR_A or letter_number > CHAR_Z):
        return "Invalid number and invalid symbol"
    if size <= 0 or size > 42:
        return "Invalid number"
    if letter_number < CHAR_A or letter_number > CHAR_Z:
        return "Invalid symbol"

    result = ""
    for x in range(size):
        for y in range(size):
            result += chr(letter_number) + " "
            letter_number = increase_letter_number(letter_number)
        result += "\n"
    return result

result = magic_square(3, 'X')
print(result)