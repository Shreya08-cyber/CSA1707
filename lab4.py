import itertools

def solve_cryptarithmetic():
    # Letters involved in SEND + MORE = MONEY
    letters = tuple('SENDMORTY')
    digits = range(10)
    
    for perm in itertools.permutations(digits, len(letters)):
        # Leading letters 'S' and 'M' cannot be 0
        if perm[letters.index('S')] == 0 or perm[letters.index('M')] == 0:
            continue
            
        trans = str.maketrans(''.join(letters), ''.join(map(str, perm)))
        send = int("SEND".translate(trans))
        more = int("MORE".translate(trans))
        money = int("MONEY".translate(trans))
        
        if send + more == money:
            return f"Solution Found:\nSEND ({send}) + MORE ({more}) = MONEY ({money})"
            
    return "No solution found"

print(solve_cryptarithmetic())
