t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    a.sort()
    print('YES') if a[-1]+a[-2]>=10 else print('NO')
    