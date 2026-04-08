import sys
input = sys.stdin.readline

def divide_decimal_string_by_2(s: str) -> str:
    """Return the quotient of decimal‐string s // 2, no leading zeros (except '0')."""
    carry = 0
    output = []
    for ch in s:
        digit = carry * 10 + (ord(ch) - ord('0'))
        q = digit // 2
        carry = digit % 2
        if output or q != 0:
            output.append(chr(q + ord('0')))
    return ''.join(output) if output else '0'

def is_divisible_by_2(s: str) -> bool:
    return (ord(s[-1]) - ord('0')) % 2 == 0

def digit_sum_mod3(s: str) -> int:
    total = 0
    for ch in s:
        total += (ord(ch) - ord('0'))
    return total % 3

def divide_decimal_string_by_3(s: str) -> str:
    """Return the quotient of decimal‐string s // 3, no leading zeros (except '0')."""
    carry = 0
    output = []
    for ch in s:
        digit = carry * 10 + (ord(ch) - ord('0'))
        q = digit // 3
        carry = digit % 3
        if output or q != 0:
            output.append(chr(q + ord('0')))
    return ''.join(output) if output else '0'

# 1) Read the decimal string for n:
S = input().strip()

# 2) Compute k = min(18, v₂(n))
k = 0
for _ in range(19):                  # do at most 19 attempts
    if is_divisible_by_2(S):
        k += 1
        S = divide_decimal_string_by_2(S)
    else:
        break
    
if k > 18:
    k = 18

# 3) Compute t = min(2, v₃(n_after_stripping_2s))
t = 0
for _ in range(2):  # at most two divisions by 3
    if digit_sum_mod3(S) == 0:
        t += 1
        S = divide_decimal_string_by_3(S)
    else:
        break

print(f"{k} {t}")
