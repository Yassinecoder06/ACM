def can_place(friends, k, x, min_dist):
    """Check if we can place k teleports such that all friends are within min_dist of a teleport"""
    friends_sorted = sorted(set(friends))
    teleports = []
    
    for friend_pos in friends_sorted:
        # Check if this friend is already covered by an existing teleport
        covered = False
        for tp in teleports:
            if abs(friend_pos - tp) <= min_dist:
                covered = True
                break
        
        if not covered:
            # Place a teleport as far right as possible while covering this friend
            teleport_pos = friend_pos + min_dist
            teleport_pos = min(teleport_pos, x)
            teleports.append(teleport_pos)
    
    if len(teleports) > k:
        return False, []
    
    # Pad with additional teleports at boundaries
    if len(teleports) < k:
        remaining = k - len(teleports)
        # Add teleports from x down to 0, avoiding duplicates
        for pos in range(x, -1, -1):
            if pos not in teleports and remaining > 0:
                teleports.append(pos)
                remaining -= 1
    
    return True, sorted(teleports)

def solve(n, k, x, friends):
    """Find k teleport positions that maximize minimum distance"""
    # Binary search on the answer
    left, right = 0, x
    best_teleports = []
    
    while left <= right:
        mid = (left + right) // 2
        can_do, teleports = can_place(friends, k, x, mid)
        
        if can_do:
            best_teleports = teleports
            left = mid + 1
        else:
            right = mid - 1
    
    return best_teleports

t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    friends = list(map(int, input().split()))
    
    result = solve(n, k, x, friends)
    print(' '.join(map(str, result)))
    