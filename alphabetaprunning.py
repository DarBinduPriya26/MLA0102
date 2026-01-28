# Alpha-Beta Pruning in Python

import math

def alphabeta(node, depth, alpha, beta, maximizingPlayer):
    # Terminal node values
    if depth == 0:
        return node

    if maximizingPlayer:
        maxEval = -math.inf
        for child in node:
            eval = alphabeta(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break   # Beta cut-off
        return maxEval
    else:
        minEval = math.inf
        for child in node:
            eval = alphabeta(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break   # Alpha cut-off
        return minEval


# Tree definition (same structure as your diagram)
tree = [
    [   # B (MIN)
        [2, 3],      # D (MAX)
        [5, 9]       # E (MAX)
    ],
    [   # C (MIN)
        [0, 1],      # F (MAX)
        [7, 5]       # G (MAX)
    ]
]

# Run Alpha-Beta
result = alphabeta(tree, 3, -math.inf, math.inf, True)

print("Optimal value using Alpha-Beta Pruning:", result)
