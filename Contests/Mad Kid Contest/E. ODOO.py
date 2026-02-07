t = int(input())

def simulation(ch: list) -> int:
    target = list("ODOO")
    minutes = 0
    for i in range(4):
        if ch[i] == target[i]:
            continue
        minutes+=1
    return minutes

for _ in range(t):
    s = input().strip()
    a = list(s)

    simulations = []
    for i in range(len(a) - 3):  
        simulations.append(simulation(a[i:i+4]))

    result = min(simulations) + len(a) - 4
    print(result)
