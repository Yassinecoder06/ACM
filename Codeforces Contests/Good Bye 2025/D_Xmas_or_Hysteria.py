import sys

# Increase recursion depth just in case, though not needed for this iterative solution
sys.setrecursionlimit(2000)

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        num_test_cases = int(next(iterator))
    except StopIteration:
        return
        
    results = []
    
    for _ in range(num_test_cases):
        try:
            n = int(next(iterator))
            m = int(next(iterator))
            a = []
            for i in range(n):
                val = int(next(iterator))
                a.append((val, i + 1))
        except StopIteration:
            break
            
        # Case m=0: Impossible because the strongest elf can never be killed
        # (anyone attacking it dies, and if it attacks anyone, it wins)
        if m == 0:
            results.append("-1")
            continue
            
        # Case m=1: Possible by having everyone else attack the strongest elf
        if m == 1:
            # Find max element
            max_val = -1
            max_idx = -1
            for val, idx in a:
                if val > max_val:
                    max_val = val
                    max_idx = idx
            
            # Everyone else attacks max
            res = []
            res.append(f"{n-1}")
            for val, idx in a:
                if idx != max_idx:
                    res.append(f"{idx} {max_idx}")
            results.append("\n".join(res))
            continue
            
        # Case m >= 2:
        # We need m survivors. All survivors must have attacked (termination condition).
        # This requires m attacks initiated by survivors.
        # Each attack kills 1 elf.
        # So we need at least m elves to die from these attacks.
        # Plus we might have other deaths.
        # But crucially, we need m distinct attackers who survive.
        # And we need m distinct victims for them.
        # So we need 2m distinct elves involved in these "survival" attacks.
        # Thus 2m <= n is required.
        if 2 * m > n:
            results.append("-1")
            continue
            
        # Strategy for m >= 2, 2m <= n:
        # 1. Pick m strongest elves to be survivors (S).
        # 2. Pick m smallest elves to be victims (V).
        # 3. Have S[i] attack V[i]. Since S are largest and V are smallest, S wins.
        # 4. Remaining n - 2m elves (R) must also die.
        #    Have them attack the strongest elf (who is in S). They will die.
        
        # Sort by value
        a.sort()
        
        # V: smallest m
        V = a[:m]
        # S: largest m
        S = a[n-m:]
        # R: middle n - 2m
        R = a[m:n-m]
        
        # Max elf is the last one in S (and globally)
        max_elf_idx = S[-1][1]
        
        attacks = []
        
        # Phase 1: S attacks V
        # We pair S[i] with V[i]
        # S is sorted ascending, V is sorted ascending
        # S[i] > V[i] is guaranteed because 2m <= n implies max(V) < min(S)
        for i in range(m):
            attacker = S[i][1]
            victim = V[i][1]
            attacks.append(f"{attacker} {victim}")
            
        # Phase 2: R attacks max_elf
        # max_elf is in S, so it has already attacked in Phase 1.
        # But it can still be a victim.
        # Since it's the strongest, anyone attacking it dies.
        for i in range(len(R)):
            attacker = R[i][1]
            victim = max_elf_idx
            attacks.append(f"{attacker} {victim}")
            
        results.append(f"{len(attacks)}")
        results.append("\n".join(attacks))

    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()
