import heapq

def a_star_search(start, goal, graph, heuristic):
    open_set = []
    # Priority queue stores tuples of: (f_score, g_score, current_node, path)
    heapq.heappush(open_set, (0 + heuristic[start], 0, start, [start]))
    g_scores = {start: 0}
    
    while open_set:
        _, current_g, current, path = heapq.heappop(open_set)
        
        if current == goal:
            return path, current_g
            
        for neighbor, weight in graph[current].items():
            tentative_g = current_g + weight
            
            if neighbor not in g_scores or tentative_g < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + heuristic[neighbor]
                heapq.heappush(open_set, (f_score, tentative_g, neighbor, path + [neighbor]))
                
    return None, float('inf')

# Graph and Heuristic values
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1}
}

heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 5, 'E': 2, 'F': 0}

path, cost = a_star_search('A', 'F', graph, heuristic)
print(f"A* Optimal Path: {path} with Total Cost: {cost}")
