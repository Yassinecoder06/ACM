import sys


def max_divisible_by_11(x: str) -> int:
    n = len(x)
    if n == 0:
        return 0

    a = [ord(c) - 48 for c in x]

    # prefix alternating sum mod 11: pref[i] = sum_{k=0..i-1} a[k]*(-1)^k  (mod 11)
    pref = [0] * (n + 1)
    sign = 1
    for i in range(n):
        pref[i + 1] = (pref[i] + sign * a[i]) % 11
        sign = -sign

    # next non-zero index from i (or n if none)
    next_nz = [0] * (n + 1)
    next_nz[n] = n
    for i in range(n - 1, -1, -1):
        if a[i] != 0:
            next_nz[i] = i
        else:
            next_nz[i] = next_nz[i + 1]

    s_pref = pref  # local alias
    s_next_nz = next_nz
    s_x = x
    # Search lengths from longest to shortest to stop early when we find any
    for L in range(n, 0, -1):
        best_s = -1
        best_eff_len = -1
        best_eff_start = -1
        found = False
        end_limit = n - L
        for s in range(0, end_limit + 1):
            # substring s .. s+L-1 divisible by 11 iff pref[s+L]-pref[s] == 0 (mod 11)
            if (s_pref[s + L] - s_pref[s]) % 11 != 0:
                continue

            # compute effective numeric substring (strip leading zeros) quickly
            nz = s_next_nz[s]
            if nz >= s + L:
                eff_len = 0
                eff_start = s + L  # canonical for zero
            else:
                eff_len = s + L - nz
                eff_start = nz

            if best_s == -1:
                best_s = s
                best_eff_len = eff_len
                best_eff_start = eff_start
                found = True
            else:
                # compare numeric values without converting to int when possible
                if eff_len > best_eff_len:
                    best_s = s
                    best_eff_len = eff_len
                    best_eff_start = eff_start
                elif eff_len == best_eff_len:
                    if eff_len == 0:
                        # both zero -> equal, keep existing
                        pass
                    else:
                        # compare the effective substrings lexicographically
                        # they have equal length and no leading zeros
                        a_sub = s_x[eff_start: s + L]
                        b_sub = s_x[best_eff_start: best_s + L]
                        if a_sub > b_sub:
                            best_s = s
                            best_eff_start = eff_start
                            # best_eff_len unchanged

        if found:
            # produce integer value for the best substring
            if best_eff_len == 0:
                return 0
            val_str = s_x[best_eff_start: best_s + L]
            # int conversion happens only once for the result
            return int(val_str)

    return 0


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        x = next(it).strip()
        out_lines.append(str(max_divisible_by_11(x)))
    sys.stdout.write("\n".join(out_lines))


if __name__ == '__main__':
    main()
            