
memo = {}
def make(length):
    if length==1:
        memo[length] = [1,0]

    else:
        if length-1 not in memo:
            make(length-1)
        
        first_half = []
        for i in memo[length-1]:
            first_half.append(2*i+1)

        second_half = []
        for i in range(0,2**(length-1)):
            second_half.append(2*i)

        memo[length] = first_half+second_half


make(16)

t = int(input())

for _ in range(t):
    n = int(input())
    result = memo[n]
    result = list(map(str, result))

    print(' '.join(result))