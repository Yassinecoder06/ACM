import sys
input = sys.stdin.readline

x = input().strip()                
result = []
if x[0] == "9":
    result.append("9")
    for ch in x[1:]:
        digit = int(ch)
        if digit >= 5:
            result.append(str(9 - digit))
        else:
            result.append(ch)
else:
    for ch in x:
        digit = int(ch)
        if digit >= 5:
            result.append(str(9 - digit))
        else:
            result.append(ch)

print("".join(result))
