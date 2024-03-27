def isValid(s: str) -> bool:
    map = {
    "(":")",
    "{":"}",
    "[":"]",
    }

    stack = []
    for paren in list(s):
        if paren in map:
            stack.append(paren)
        elif len(stack) == 0 or paren != map[stack.pop()]:
                return False
    
    return len(stack) == 0


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))