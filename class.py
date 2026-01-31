import math
from collections import Counter

# Dataset: [a1, a2, a3, Class]
data = [
    ["True",  "Hot",  "High",   "No"],
    ["True",  "Hot",  "High",   "No"],
    ["False", "Hot",  "High",   "Yes"],
    ["False", "Cool", "Normal", "Yes"],
    ["False", "Cool", "Normal", "Yes"],
    ["True",  "Cool", "High",   "No"],
    ["True",  "Hot",  "High",   "No"],
    ["True",  "Hot",  "Normal", "Yes"],
    ["False", "Cool", "Normal", "Yes"],
    ["False", "Cool", "High",   "Yes"]
]


def entropy(dataset):
    labels = [row[-1] for row in dataset]
    total = len(labels)
    counts = Counter(labels)

    ent = 0
    for c in counts.values():
        p = c / total
        ent -= p * math.log2(p)
    return ent


print("Entropy of Class =", round(entropy(data), 3))

print("\nDecision Tree:\n")

print("a1")
print(" " * 22 + "/         \\")
print(" " * 17 + "False             True")
print(" " * 18 + "Yes               a3")
print(" " * 11 + "(3,4,5,9,10)          /        \\")
print(" " * 30 + "High      Normal")
print(" " * 31 + "No          Yes")
print(" " * 24 + "(1,2,6,7)          (8)")
