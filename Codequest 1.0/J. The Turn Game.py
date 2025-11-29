n = int(input())
a = input()
b = input()
turn = "Luffy"


for i in range(n):
    if a[i] < b[i]:
        if turn == "Luffy":
            turn = "Zoro"
        else:
            turn = "Luffy"
    if a[i] == b[i]:
        break

print(turn)