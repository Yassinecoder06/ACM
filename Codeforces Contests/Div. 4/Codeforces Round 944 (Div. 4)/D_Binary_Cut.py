t = int(input())

for _ in range(t):
    s = list(input())

    groups = 1
    has01 = 0

    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            groups += 1
        if s[i] == '1' and s[i-1] == '0':
            has01 = 1

    print(groups-has01)