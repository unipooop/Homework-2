import math

# Define the liquidity dictionary
liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

def find_profitable_path(liquidity):
    # Initialize variables to store the best path and balance
    best_path = None
    best_balance = -math.inf

    # Iterate over all possible paths
    for start, end in liquidity:
        # Check if there is a reverse path
        if (end, start) in liquidity:
            # Calculate the profit ratio for the current path
            ratio = liquidity[end, start][0] / liquidity[start, end][1]
            
            # Check if this path is profitable
            if ratio > 1:
                # Calculate the balance for tokenB
                balance = liquidity[start, end][1] * ratio - liquidity[start, end][0]
                
                # Check if this balance is better than the current best balance
                if balance > best_balance:
                    best_balance = balance
                    best_path = [start, end]

    return best_path, best_balance

def print_path(path, balance):
    # Print the path in the specified format
    if path:
        print(f"path: {'->'.join(path)}, tokenB balance={balance:.6f}")
    else:
        print("No profitable path found.")

# Find the profitable path and balance
profitable_path, balance = find_profitable_path(liquidity)

# Print the result
print_path(profitable_path, balance)
