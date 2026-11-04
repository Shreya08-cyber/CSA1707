def is_valid(node, color, assignment, graph):
    """Check if the color assignment is valid for the given node."""
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment, graph, colors):
    """Recursive backtracking function for CSP map coloring."""
    if len(assignment) == len(graph):
        return assignment
    
    # Select unassigned variable
    unassigned = [n for n in graph if n not in assignment]
    node = unassigned[0]
    
    for color in colors:
        if is_valid(node, color, assignment, graph):
            assignment[node] = color
            result = backtrack(assignment, graph, colors)
            if result:
                return result
            del assignment[node]
            
    return None

# Graph representation of Australian territories
graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}
colors = ['Red', 'Green', 'Blue']

solution = backtrack({}, graph, colors)
print("Map Coloring Solution:", solution)
