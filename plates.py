
def is_valid(s):
    # Check if the first two characters are letters
    if not s[:2].isalpha():
        return False
    
    # Check length
    if not (2 <= len(s) <= 6):
        return False
    
    # Check for invalid characters
    if not s.isalnum():
        return False
    
    # Check if numbers are at the end and the first number is not '0'
    num_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not num_started and char == '0':
                return False
            num_started = True
        elif num_started:
            # If a letter comes after a number, it's invalid
            return False
    
    return True




# The first number used cannot be a ‘0’.”
#“No periods, spaces, or punctuation marks are allowed.”


#In plates.py, implement a program that prompts the user for a vanity plate and then 
# output Valid if meets all of the requirements or Invalid if it does not. 
# Assume that any letters in the user’s input will be uppercase. 
# Structure your program per the below, wherein is_valid returns True if s meets all 
# requirements and False if it does not. 
# Assume that s will be a str. You’re welcome to implement additional 
# functions for is_valid to call (e.g., one function per requirement).



#Run your program with python plates.py. Type CS50 and press Enter. Your program should output:
#Valid
#Run your program with python plates.py. Type python plates.py and press Enter. Your program should output:
#Invalid
#Run your program with python plates.py. Type CS50P and press Enter. Your program should output
#Invalid
#Run your program with python plates.py. Type PI3.14 and press Enter. Your program should output
#Invalid
#Run your program with python plates.py. Type H and press Enter. Your program should output
#Invalid
#Run your program with python plates.py. Type OUTATIME and press Enter. Your program should output
#Invalid






