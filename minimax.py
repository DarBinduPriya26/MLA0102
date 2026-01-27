# Minimax Algorithm Implementation

def minimax(depth, nodeIndex, isMax, scores, height):
    # If we reach a leaf node
    if depth == height:
        return scores[nodeIndex]

    if isMax:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, scores, height),
            minimax(depth + 1, nodeIndex * 2 + 1, False, scores, height)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, scores, height),
            minimax(depth + 1, nodeIndex * 2 + 1, True, scores, height)
        )


# Leaf node values (from your diagram, left to right)
scores = [2, 3, 5, 9, 0, 1, 7, 5]

import math
height = int(math.log2(len(scores)))

# Root node is Max
optimal_value = minimax(0, 0, True, scores, height)

print("The optimal value is:", optimal_value)
