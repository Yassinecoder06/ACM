MOD = 998244353

import sys

def main():
    t = int(input())
    out_lines = []
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        q = list(map(int, input().split()))
        
        A = [1] * n
        for i in range(n):
            exp = p[i]
            if exp == 0:
                A[i] = 1
            else:
                A[i] = pow(2, exp, MOD)
        
        B = [1] * n
        for i in range(n):
            exp = q[i]
            if exp == 0:
                B[i] = 1
            else:
                B[i] = pow(2, exp, MOD)
        
        sortedA = sorted([(A[i], i) for i in range(n)], reverse=True)
        sortedB = sorted([(B[i], i) for i in range(n)], reverse=True)
        
        res = [0] * n
        for i in range(n):
            best = -1
            ptrA = 0
            ptrB = 0
            seen = set()
            for _ in range(min(5, (i+1))):
                candidate_val = -1
                candidate_j = -1
                while ptrA < len(sortedA) and sortedA[ptrA][1] > i:
                    ptrA += 1
                while ptrB < len(sortedB) and sortedB[ptrB][1] > i:
                    ptrB += 1
                if ptrA < len(sortedA) and (ptrB >= len(sortedB) or sortedA[ptrA][0] >= sortedB[ptrB][0]):
                    a_val, a_idx = sortedA[ptrA]
                    j = a_idx
                    k = i - j
                    if k < 0 or k > i:
                        ptrA += 1
                        continue
                    if k < n and k >= 0:
                        s = (a_val + B[k]) % MOD
                        if s > candidate_val:
                            candidate_val = s
                            candidate_j = j
                    ptrA += 1
                else:
                    if ptrB < len(sortedB):
                        b_val, b_idx = sortedB[ptrB]
                        k = b_idx
                        j = i - k
                        if j < 0 or j > i:
                            ptrB += 1
                            continue
                        if j < n and j >= 0:
                            s = (A[j] + b_val) % MOD
                            if s > candidate_val:
                                candidate_val = s
                                candidate_j = j
                        ptrB += 1
                if candidate_j != -1 and candidate_val > best:
                    best = candidate_val
                if candidate_j != -1:
                    seen.add(candidate_j)
            res[i] = best
        out_lines.append(" ".join(map(str, res)))
    print("\n".join(out_lines))

main()