t = int(input())

for _ in range(t):
    n, k, p, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    win_idx = p - 1  # 0-indexed position of win-condition
    win_cost = a[win_idx]
    
    # Deck as list of (cost, is_win_condition)
    deck = [(a[i], i == win_idx) for i in range(n)]
    
    energy = m
    plays = 0
    
    while energy > 0:
        # Find current position of win-condition
        win_pos = -1
        for i in range(len(deck)):
            if deck[i][1]:
                win_pos = i
                break
        
        if win_pos == -1:
            break
        
        if win_pos < k:
            # Win-condition is playable
            if energy < win_cost:
                break
            energy -= win_cost
            plays += 1
            
            # Move win-condition to end of deck
            card = deck.pop(win_pos)
            deck.append(card)
        else:
            # Need to play filler - find cheapest in first k positions
            min_cost = float('inf')
            min_pos = -1
            for i in range(min(k, len(deck))):
                if not deck[i][1] and deck[i][0] < min_cost:
                    min_cost = deck[i][0]
                    min_pos = i
            
            # No playable filler available or can't afford it
            if min_pos == -1 or min_cost > energy:
                break
            
            energy -= min_cost
            # Move filler to end of deck
            card = deck.pop(min_pos)
            deck.append(card)
    
    print(plays)

