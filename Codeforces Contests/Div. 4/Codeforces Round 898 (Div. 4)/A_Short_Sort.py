t = int(input())

for _ in range(t):
    s = input()
    target = "abc"

    diff = 0
    for i in range(3):
        if s[i] == target[i]:
            diff += 1

    
    print("YES") if diff >= 1 else print("NO")