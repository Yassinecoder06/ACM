t = int(input())


def simulation(array):
    result = []
    meat = 0
    start = False
    for ch in array:
        if ch == ".":
            start = True
        if ch == "#" and start:
            meat +=1
        if ch == "|" and start:
            result.append(meat)
            meat = 0
            start = False
    result.append(meat)
    return max(result)

for _ in range(t):
    n = int(input())
    a = list(input())

    print(max(simulation(a), simulation(a[::-1])))

    
