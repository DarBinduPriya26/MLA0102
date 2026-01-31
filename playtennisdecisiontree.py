import math
from collections import Counter, defaultdict

# Dataset
data = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Sunny", "Hot", "High", "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Strong", "No"],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"],
    ["Sunny", "Mild", "High", "Weak", "No"],
    ["Sunny", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "Normal", "Weak", "Yes"],
    ["Sunny", "Mild", "Normal", "Strong", "Yes"],
    ["Overcast", "Mild", "High", "Strong", "Yes"],
    ["Overcast", "Hot", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Strong", "No"]
]

attributes = ["Outlook", "Temperature", "Humidity", "Wind"]

# Entropy function
def entropy(data):
    labels = [row[-1] for row in data]
    counts = Counter(labels)
    total = len(data)
    ent = 0
    for c in counts.values():
        p = c / total
        ent -= p * math.log2(p)
    return ent

# Information Gain
def information_gain(data, attr_index):
    total_entropy = entropy(data)
    subsets = defaultdict(list)

    for row in data:
        subsets[row[attr_index]].append(row)

    weighted_entropy = 0
    for subset in subsets.values():
        weighted_entropy += (len(subset) / len(data)) * entropy(subset)

    return total_entropy - weighted_entropy

# ID3 Algorithm
def id3(data, attributes):
    labels = [row[-1] for row in data]

    # If all same class
    if labels.count(labels[0]) == len(labels):
        return labels[0]

    # If no attributes left
    if not attributes:
        return Counter(labels).most_common(1)[0][0]

    # Choose best attribute
    gains = [information_gain(data, i) for i in range(len(attributes))]
    best_attr_index = gains.index(max(gains))
    best_attr = attributes[best_attr_index]

    tree = {best_attr: {}}

    attr_values = set(row[best_attr_index] for row in data)

    for value in attr_values:
        subset = [row[:best_attr_index] + row[best_attr_index+1:]
                  for row in data if row[best_attr_index] == value]

        subtree = id3(
            subset,
            attributes[:best_attr_index] + attributes[best_attr_index+1:]
        )

        tree[best_attr][value] = subtree

    return tree

# Print tree nicely
def print_tree(tree, indent=""):
    if not isinstance(tree, dict):
        print(indent + "→", tree)
        return

    for key, value in tree.items():
        for subkey, subtree in value.items():
            print(indent + f"{key} = {subkey}")
            print_tree(subtree, indent + "   ")

# Build tree
decision_tree = id3(data, attributes)

# Output
print("Entropy of PlayTennis:", round(entropy(data), 3))
print("\nDecision Tree:\n")
print_tree(decision_tree)
