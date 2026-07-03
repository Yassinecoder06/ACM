t = int(input())

for _ in range(t):
    a1,a2,b1,b2 = list(map(int, input().split()))
    
    games = [
        ((a1, b1), (a2, b2)),
        ((a1, b2), (a2, b1)),
        ((a2, b1), (a1, b2)),
        ((a2, b2), (a1, b1)),
    ]

    won_games = 0

    for game in games:
        suneet_wins = 0
        slavic_wins = 0
        
        for round in game:
            if round[0] > round[1]:
                suneet_wins += 1
            elif round[1] > round[0]:
                slavic_wins += 1
        
        if suneet_wins > slavic_wins:
            won_games += 1
    
    print(won_games)