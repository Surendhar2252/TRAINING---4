def queensAttack(n, k, r_q, c_q, obstacles):
    directions = {
        'n': (1, 0), 's': (-1, 0), 'e': (0, 1), 'w': (0, -1),
        'ne': (1, 1), 'nw': (1, -1), 'se': (-1, 1), 'sw': (-1, -1)
    }
    
    obstacles = {(r, c) for r, c in obstacles}
    count = 0
    
    for direction in directions.values():
        r, c = r_q + direction[0], c_q + direction[1]
        
        while 1 <= r <= n and 1 <= c <= n and (r, c) not in obstacles:
            count += 1
            r += direction[0]
            c += direction[1]
            
    return count
