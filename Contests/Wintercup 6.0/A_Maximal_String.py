t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    stack = []
    for c in s:
        stack.append(c)
        while len(stack) >= 2:
            a, b = stack[-2], stack[-1]
            if a == b:
                if a == '0':
                    stack.pop()
                    stack.pop()
                    stack.append('1')
                else:
                    if len(stack) >= 3 and stack[-3] == '0':
                        stack.pop()
                        stack.pop()
                        stack.append('0')
                        if len(stack) >= 2 and stack[-2] == stack[-1] == '0':
                            stack.pop()
                            stack.pop()
                            stack.append('1')
                        else:
                            break
                    else:
                        break
            else:
                break
    print(''.join(stack))

        
    

