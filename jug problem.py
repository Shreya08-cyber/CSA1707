from collections import deque

def solve_water_jug_exact(cap_j1, cap_j2, target_j1):
    """
    Finds the shortest sequence of actions to measure 'target_j1' liters 
    specifically inside Jug 1.
    """
    # Queue stores: ((j1_amount, j2_amount), [list of (action_description, state)])
    start_state = (0, 0)
    queue = deque([ (start_state, [("Initial State", start_state)]) ])
    visited = set([start_state])

    while queue:
        (j1, j2), path = queue.popleft()

        # Goal Condition: Jug 1 must have exactly target_j1 liters
        if j1 == target_j1:
            return path

        # All possible operations and their resulting states
        pour_1_to_2 = min(j1, cap_j2 - j2)
        pour_2_to_1 = min(j2, cap_j1 - j1)

        possible_moves = [
            (f"Fill Jug 1", (cap_j1, j2)),
            (f"Fill Jug 2", (j1, cap_j2)),
            (f"Empty Jug 1", (0, j2)),
            (f"Empty Jug 2", (j1, 0)),
            (f"Pour Jug 1 -> Jug 2 ({pour_1_to_2}L)", (j1 - pour_1_to_2, j2 + pour_1_to_2)),
            (f"Pour Jug 2 -> Jug 1 ({pour_2_to_1}L)", (j1 + pour_2_to_1, j2 - pour_2_to_1))
        ]

        # Explore unvisited states
        for action, next_state in possible_moves:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(action, next_state)]))

    return None

# --- Example Usage (4L Jug, 3L Jug, Goal: Exactly 2L in Jug 1) ---
if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target_in_jug1 = 2

    solution = solve_water_jug_exact(jug1_capacity, jug2_capacity, target_in_jug1)

    if solution:
        print(f"Goal Reached! Solved in {len(solution) - 1} steps:\n")
        for idx, (action, (j1, j2)) in enumerate(solution):
            print(f"Step {idx}: {action:<25} -> Jug 1: {j1}L | Jug 2: {j2}L")
    else:
        print("No solution possible for these capacities and target.")
