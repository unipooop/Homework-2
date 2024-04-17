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
def execute_swap(liquidity, amount, token_in, token_out):
    if (token_in, token_out) in liquidity:
        reserve_in, reserve_out = liquidity[(token_in, token_out)]
    else:
        reserve_out, reserve_in = liquidity[(token_out, token_in)]

    product_reserves = reserve_in * reserve_out
    new_reserve_in = reserve_in + amount
    new_reserve_out = product_reserves / new_reserve_in
    output_amount = reserve_out - new_reserve_out

    if (token_in, token_out) in liquidity:
        liquidity[(token_in, token_out)] = [new_reserve_in, new_reserve_out]
    else:
        liquidity[(token_out, token_in)] = [new_reserve_out, new_reserve_in]
    
    return output_amount

def find_optimal_sequence(liquidity, initial_amount, current_token, target_amount, target_token, sequence, depth, max_depth):
    if depth > max_depth:
        return None, []

    possible_swaps = [key for key in liquidity.keys() if current_token in key]
    results = []
    for swap in possible_swaps:
        other_token = swap[0] if swap[1] == current_token else swap[1]
        updated_liquidity = liquidity.copy()
        swapped_amount = execute_swap(updated_liquidity, initial_amount, current_token, other_token)
        if other_token == target_token and round(swapped_amount) == target_amount:
            return swapped_amount, sequence + [(current_token, other_token)]
        elif other_token != target_token:
            result_amount, result_sequence = find_optimal_sequence(updated_liquidity, swapped_amount, other_token, target_amount, target_token, sequence + [(current_token, other_token)], depth + 1, max_depth)
            if result_amount is not None:
                results.append((result_amount, result_sequence))
    if results:
        results.sort(key=lambda x: abs(target_amount - x[0]))
        return results[0]
    return None, []

max_search_depth = 7

start_token = 'tokenB'
final_amount, best_path = find_optimal_sequence(liquidity, 5, start_token, 21, start_token, [], 0, max_search_depth)
print("Optimal path from tokenB:", end='')
for pair in best_path:
    print('->'+pair[1], end='')
print(", tokenB balance after trade:", final_amount, '.')
