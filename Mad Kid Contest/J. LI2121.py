a,b,c = map(int, input().split())
m = int(input())

usb = []
ps2 = []

for _ in range(m):
    val, typ = input().split()
    val = int(val)
    if typ == "USB":
        usb.append(val)
    else:            
        ps2.append(val)

usb.sort()
ps2.sort()

total_cost = 0
equipped = 0

for i in range(min(a, len(usb))):
    total_cost += usb[i]
    equipped += 1

usb = usb[min(a, len(usb)):]  

for i in range(min(b, len(ps2))):
    total_cost += ps2[i]
    equipped += 1

ps2 = ps2[min(b, len(ps2)):]  

remaining = sorted(usb + ps2)
for i in range(min(c, len(remaining))):
    total_cost += remaining[i]
    equipped += 1

print(equipped, total_cost)
