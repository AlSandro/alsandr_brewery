

"""

Hommade lower() and upper() 


"""
def toLowerCase(str: str):
    diff = ord("a") - ord('A')  # differnce betwen lower and uppder in ascii 
    lower_string_chars = [] # placeholder for the lowercase 
    for character in str:
        if "A" <= character <= "Z": # if the character in Capital chars
            lower_string_chars.append(chr(ord(character) + diff))
        else:
            lower_string_chars.append(character)
    # print(new_string_chars)
    return "".join(lower_string_chars) 

def toUpperCase(str: str):
    diff = ord("a") - ord('A')  # differnce betwen lower and uppder in ascii 
    upper_string_chars = [] # placeholder for the uppercase 
    for character in str:
        if "a" <= character <= "z": # if the character in Capital chars
            upper_string_chars.append(chr(ord(character) - diff))
        else:
            upper_string_chars.append(character)
    # print(new_string_chars)
    return "".join(upper_string_chars) 

# Test here
print(toLowerCase('Hello World!!!'))
print(toUpperCase('Hello World!!!'))