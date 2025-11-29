t = int(input())
for _ in range(t):
    n = int(input())
    result = []
    for i in range(n):
        s = input()
        result.append(str(s.find("#")+1))
    result=result[::-1]
    print(" ".join(result))


