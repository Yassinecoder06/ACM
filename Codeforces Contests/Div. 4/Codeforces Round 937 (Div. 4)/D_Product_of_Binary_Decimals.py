t = int(input())


binaries = []
for i in range(1, 64):
    b_val = int(bin(i)[2:])
    if b_val > 1:
        binaries.append(b_val)

binaries.sort(reverse=True)


def can_decompose(n):
    if n == 1:
        return True
    
    for b in binaries:
        if b > n:
            continue
        if n % b == 0:
            if can_decompose(n // b):
                return True
    return False

    
for _ in range(t):
    n = int(input())
    if can_decompose(n):
        print("YES")
    else:
        print("NO")