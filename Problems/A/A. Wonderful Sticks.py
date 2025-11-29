t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    sorted_list = [i for i in range(1, n+1)]
    output =  [0]*n
    for i in range(n-2,-1,-1):
        if s[i] == '>':
            output[i+1] = sorted_list[-1]
            sorted_list.pop()
        elif s[i] == '<':
            output[i+1] = sorted_list[0]
            sorted_list.pop(0)
    output[0] = sorted_list[0]
    for i in range(n):
        output[i] = str(output[i])
    print(" ".join(output))

#Accepted