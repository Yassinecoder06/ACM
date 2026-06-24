t = int(input())

for _ in range(t):
    n,k = map(int, input().split())

    s = set(map(int, input().split()))
    t = set(map(int, input().split()))

    common_numbers = set(s).intersection(set(t))

    s = [num for num in s if num not in common_numbers]
    t = [num for num in t if num not in common_numbers]
    s.sort()
    t.sort()

    #creating zouz t

    t1 = [num+k for num in t]
    t2 = [abs(num-k) for num in t]
    ok = True
    for i in range(len(s)):
        if not(s[i] == t1[i] or s[i] == t2[i]):
            ok = False
            break

    if ok:
        print("YES")
    else:
        print("NO")