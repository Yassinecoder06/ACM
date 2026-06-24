import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    s = input().strip()

    s = "1" + s + "1"

    ans = 0
    l = 0

    for i in range(1, n + 1):
        if s[i] == '0':
            if s[i - 1] == '1':
                l = i

            if s[i + 1] == '1':
                c = (l == 1) + (i == n)
                ans += (i - l + 1 + c) // 3

        else:
            ans += 1

    print(ans)


t = int(input())
for _ in range(t):
    solve()