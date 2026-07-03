t = int(input())

for _ in range(t):
    n,k = map(int, input().split())

    count = n-1
    skip = k // count
    rest = k % count
    number = skip * n
    if rest == 0:
        rest -= 1
    print(rest+number)