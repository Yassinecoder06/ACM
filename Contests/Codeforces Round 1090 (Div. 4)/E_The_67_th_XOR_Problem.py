import sys

def max_xor_subset(arr):
    basis = [0]*31
    
    for x in arr:
        for b in reversed(range(31)):
            if not (x>>b)&1:
                continue
            if basis[b]==0:
                basis[b]=x
                break
            x ^= basis[b]
    
    res = 0
    for b in reversed(range(31)):
        res = max(res, res ^ basis[b])
        
def max_pair_xor(arr):
    ans = 0
    mask = 0

    for bit in range(30, -1, -1):
        mask |= 1 << bit
        prefixes = {x & mask for x in arr}
        candidate = ans | (1 << bit)

        if any((p ^ candidate) in prefixes for p in prefixes):
            ans = candidate

    return ans


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = data[idx:idx + n]
        idx += n
        out.append(str(max_pair_xor(arr)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()