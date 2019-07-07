
def romanToInt(s: str) -> int:
    roman_dict = {'I':1,'V':5,'X':10,'L':50, 'C':100,'D':500,'M':1000}
    final = 0 
    counter = len(s) 
    for i in range(counter-1):
        if roman_dict[s[i]] >= roman_dict[s[i+1]]:
            final += roman_dict[s[i]]
        elif roman_dict[s[i]] < roman_dict[s[i+1]]:
            roman_dict[s[i+1]] -= roman_dict[s[i]]
    return final + roman_dict[s[-1]] # something wrong here.... even though it works

print (romanToInt('MCMXCIV'))