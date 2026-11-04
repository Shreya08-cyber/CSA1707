import heapq
GOAL_STATE = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)
def manhattan_distance(state):
    """Calculates the sum of Manhattan distances of tiles from their target positions."""
    distance = 0
    for idx, value in enumerate(state):
        if value != 0:
            # Current row and column
            r1, c1 = divmod(idx, 3)
            # Target row and column
            r2, c2 = divmod(value - 1, 3)
            distance += abs(r1 - r2) + abs(c1 - c2)
    return distance
def get_neighbors(state):
    """Generates all valid next states by sliding adjacent numbers into the blank space."""
    neighbors = []
    blank_idx = state.index(0)
    row, col = divmod(blank_idx, 3)
    # Possible moves: Up, Down, Left, Right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in moves:
        r2, c2 = row + dr, col + dc
        if 0 <= r2 < 3 and 0 <= c2 < 3:
            new_blank_idx = r2 * 3 + c2
            state_list = list(state)
            # Swap blank space with adjacent tile
            state_list[blank_idx], state_list[new_blank_idx] = state_list[new_blank_idx], state_list[blank_idx]
            neighbors.append(tuple(state_list))
    return neighbors
def solve_8_puzzle(initial_state):
    """Solves the 8-puzzle using the A* Search algorithm."""
    # Priority Queue stores: (f_score, g_score, current_state, path)
    pq = []
    heapq.heappush(pq, (manhattan_distance(initial_state), 0, initial_state, [initial_state]))
    visited = set()
    while pq:
        f, g, current, path = heapq.heappop(pq)
        if current == GOAL_STATE:
            return path
        if current in visited:
            continue
        visited.add(current)
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                g_new = g + 1
                h_new = manhattan_distance(neighbor)
                f_new = g_new + h_new
                heapq.heappush(pq, (f_new, g_new, neighbor, path + [neighbor]))
    return None
def print_board(state):
    """Helper function to print a 3x3 grid nicely."""
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()
# --- Example Usage ---
if __name__ == "__main__":
    # 0 represents the blank space
    initial_board = (
        1, 2, 3,
        4, 0, 6,
        7, 5, 8
    )

    print("--- 8-Puzzle Solution ---")
    solution_path = solve_8_puzzle(initial_board)
    if solution_path:
        print(f"Solved in {len(solution_path) - 1} steps:\n")
        for step, state in enumerate(solution_path):
            print(f"Step {step}:")
            print_board(state)
    else:
        print("No solution found.")
