import numpy as np

def mp_neuron(inputs, weights, threshold):
    weighted_sum = np.dot(inputs, weights)

    if weighted_sum >= threshold:
        return 1
    else:
        return 0

def AND(x1, x2):
    return mp_neuron([x1, x2], [1, 1], 2)

def OR(x1, x2):
    return mp_neuron([x1, x2], [1, 1], 1)

def NOR(x1, x2):
    return mp_neuron([x1, x2], [-1, -1], 0)

def NOT(x):
    return mp_neuron([x], [-1], 0)

inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

print("x1 x2 |  AND   OR  NOR")
print("------------------------")

for x1, x2 in inputs:
    print(x1, " ", x2, " | ", AND(x1, x2), "  ", OR(x1, x2), "  ", NOR(x1, x2))

print("\nNOT Gate")
print("x | NOT")
print("-------")

for x in [0, 1]:
    print(x, "|", NOT(x))