t = int(input())
for _ in range(t):
    n, s = input().split()
    n = int(n)
    biggest_s = "1" * n
    print((int(biggest_s, 2) - int(s, 2)) % 2**62)