def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if not s:
        return False
    stack = []
    chars = ['(', ')', '[', ']', '{', '}']
    for c in s:
        if c in chars:
            if stack:
                if c in ')]}':
                    m = stack.pop()
                    if '}' == c:
                        t = '{'
                    elif ')' == c:
                        t = '('
                    elif ']' == c:
                        t = '['
                    else:
                        t = None
                    if m != t:
                        return False
                else:
                    stack.append(c)
            else:
                stack.append(c)
    return stack == []

s = 'hello(world), welcome to { ()} China.'
print(isValid(s))
