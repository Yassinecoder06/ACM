t = int(input())

for _ in range(t):
    s = input()
    s1= list(s[:3])
    s2= list(s[3:])
    s1 = map(int, s1)
    s2 = map(int, s2)

    if sum(s1) == sum(s2):
        print("YES")
    else:
        print("NO")
    