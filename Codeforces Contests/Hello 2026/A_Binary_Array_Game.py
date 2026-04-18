t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if a[-1] or a[0]:
        print("Alice")
    elif a[-1] == a[0] == 0:
        print("Bob")