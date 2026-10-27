def is_valid(state):
    m_left, c_left, boat = state
    m_right = 3 - m_left
    c_right = 3 - c_left
    
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 3 or c_left > 3 or m_right > 3 or c_right > 3:
        return False
    # Missionaries cannot be outnumbered by cannibals on either side
    if m_left > 0 and m_left < c_left:
        return False
    if m_right > 0 and m_right < c_right:
        return False
    return True

def missionaries_cannibals():
    # State format: (Missionaries_left, Cannibals_left, Boat_position [1=Left, 0=Right])
    initial_state = (3, 3, 1)
    target_state = (0, 0, 0)
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    
    queue = [(initial_state, [initial_state])]
    visited = set()
    
    while queue:
        current_state, path = queue.pop(0)
        if current_state == target_state:
            return path
        
        if current_state in visited:
            continue
        visited.add(current_state)
        
        m, c, boat = current_state
        for dm, dc in moves:
            if boat == 1:
                new_state = (m - dm, c - dc, 0)
            else:
                new_state = (m + dm, c + dc, 1)
                
            if is_valid(new_state) and new_state not in visited:
                queue.append((new_state, path + [new_state]))
    return None

print("Missionaries & Cannibals Solution Path:")
for step in missionaries_cannibals():
    print(step)
