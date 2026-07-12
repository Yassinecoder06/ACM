t = int(input())

def is_good(n):
    s = set(str(n))

    if len(s)>2:
        return False
    return True

for _ in range(t):
    x = int(input())

    for d in range(1,10):
        y = 10**d + 1

        if is_good(x*y):
            print(y)
            break
