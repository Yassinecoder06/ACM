t = int(input())

for _ in range(t):
    s = input()
    h_str, m = s.split(':')
    h = int(h_str)

    period = 'PM' if h >= 12 else 'AM'

    hour_12 = h % 12
    if hour_12 == 0:
        hour_12 = 12

    print(f"{hour_12:02d}:{m} {period}")