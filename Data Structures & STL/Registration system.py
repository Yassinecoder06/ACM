n = int(input())
d = dict()
for i in range(n):
    ch = input()
    if ch in d:
        d[ch] += 1
        print(f"{ch}{d[ch]}")
    else:
        d[ch] = 0
        print("OK")
        