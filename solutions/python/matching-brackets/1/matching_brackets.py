def is_paired(input_string):
    stack = []
    for char in input_string:
        if char in "[{(":
            stack.append(char)
        if char in "]})":
            if not stack:
                return False
            bracket = stack.pop()
            if bracket == "[" and char != "]":
                return False
            if bracket == "{" and char != "}":
                return False
            if bracket == "(" and char != ")":
                return False
    return not stack
            
                
            
            