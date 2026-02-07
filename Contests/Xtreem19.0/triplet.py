import sys
from collections import deque

def construct_abc_dp(N):
    # impossible cases
    if N % 2 == 1:                    # N odd -> no solution
        return None
    if (N & (N-1)) == 0:              # N is power of two -> no solution
        return None

    target_sum = 2 * N
    maxbits = max(N.bit_length(), target_sum.bit_length()) + 5

    nbits = [(N >> i) & 1 for i in range(maxbits)]
    sbits = [(target_sum >> i) & 1 for i in range(maxbits)]

    # dp[pos] : dict mapping state -> parent
    # state = (carry, eqAB, eqAC, eqBC, hasA, hasB, hasC)
    # parent stored as (prev_state, (a,b,c)) for reconstruction
    dp = [dict() for _ in range(maxbits + 1)]
    start = (0, True, True, True, False, False, False)
    dp[0][start] = None

    for pos in range(maxbits):
        for key, parent in list(dp[pos].items()):
            carry, eqAB, eqAC, eqBC, hasA, hasB, hasC = key
            # try all 8 possibilities for (a,b,c) bits at this position
            for a in (0,1):
                for b in (0,1):
                    for c in (0,1):
                        # XOR constraint for this bit
                        if (a ^ b ^ c) != nbits[pos]:
                            continue
                        total = a + b + c + carry
                        # sum bit at this position must match sbits[pos]
                        if (total & 1) != sbits[pos]:
                            continue
                        carry_out = total >> 1
                        eqAB2 = eqAB and (a == b)
                        eqAC2 = eqAC and (a == c)
                        eqBC2 = eqBC and (b == c)
                        hasA2 = hasA or (a == 1)
                        hasB2 = hasB or (b == 1)
                        hasC2 = hasC or (c == 1)
                        newkey = (carry_out, eqAB2, eqAC2, eqBC2, hasA2, hasB2, hasC2)
                        # store first parent reaching newkey (sufficient)
                        if newkey not in dp[pos + 1]:
                            dp[pos + 1][newkey] = (key, (a, b, c))

    # Look for a final state with carry=0, all three numbers positive (has* True)
    # and none of them equal (eq flags all False)
    final_key = None
    for key in dp[maxbits].keys():
        carry, eqAB, eqAC, eqBC, hasA, hasB, hasC = key
        if carry == 0 and (not (eqAB or eqAC or eqBC)) and hasA and hasB and hasC:
            final_key = key
            break

    if final_key is None:
        return None

    # Reconstruct bits (from most significant to least)
    A = B = C = 0
    key = final_key
    for pos in range(maxbits, 0, -1):
        parent, bits = dp[pos][key]
        a, b, c = bits
        A = (A << 1) | a
        B = (B << 1) | b
        C = (C << 1) | c
        key = parent

    # final sanity checks
    if A <= 0 or B <= 0 or C <= 0 or len({A, B, C}) < 3:
        return None
    if (A ^ B ^ C) != N or (A + B + C) != 2 * N:
        return None
    return (A, B, C)


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    T = int(next(it))
    out_lines = []
    for _ in range(T):
        N = int(next(it))
        triple = construct_abc_dp(N)
        if triple is None:
            out_lines.append("-1")
        else:
            A, B, C = triple
            out_lines.append(f"{A} {B} {C}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
