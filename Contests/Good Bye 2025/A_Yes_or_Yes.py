t = int(input())
for _ in range(t):
    s = input()
    print("YES" if s.count('Y') <= 1 else "NO")