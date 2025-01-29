def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if the length of the plate is between 2 and 6 characters
    if 6 >= len(s) >= 2 and s[0:2].isalpha() and s.isalnum():
        for char in s:
            if char.isdigit():
                index = s.index(char)
                if s[index:].isdigit() and char != '0':
                    return True
                else:
                    return False
        return True
main()






#“Numbers cannot be used in the middle of a plate; they must come at the end. 
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 

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






