t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    if n % 2 != 0:
        print("NO")
        continue

    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    print("YES" if not stack else "NO")
