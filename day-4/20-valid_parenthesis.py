def is_balanced(exp):
        brackets={'(':')','[':']','{':'}'}
        stack=[]
        for i in exp:
            if i in "([{":
                stack.append(i)
            elif i in ")]}":
                if len(stack)==0:
                    return False
                if brackets[stack.pop()]!=i:
                    return False
        return len(stack)==0
print(is_balanced( "()[]{}"))

