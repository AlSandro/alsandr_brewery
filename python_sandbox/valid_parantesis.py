def isValidParantesis(self, s: str) -> bool:
    open_stack = [] # we will store here any opening brackets 
    match = {'(':')','{':'}','[':']'} # dictionary with key-pair for brackets
    
    for c in s: # iterating through the array
        if c in match: # if character in the dictionary
            open_stack.append(c) # we consider it's opening and add to the opening stack 
        else: # if not 
            if not open_stack or match[open_stack.pop()] != c: # we check if the stack is empty or the last bracket in the stack matches the closing one
                return False
                
    return not open_stack # true if stack empty, means 