import numpy as np

class Perceptron:
    def __init__(self, input_size: int, lr: float = 0.1, epochs: int = 100):
        self.lr = lr
        self.epochs = epochs
        self.weights = np.zeros(input_size) #initialize weight bias to 0
        self.bias = 0.0

    def step_function(self, z: float) -> int:
        return 1 if z >= 0 else 0

    def predict(self, x: np.ndarray) -> int:
        linear_output = np.dot(x, self.weights) + self.bias
        return self.step_function(linear_output)

    def train(self, X: np.ndarray, y: np.ndarray):
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                prediction = self.predict(xi)
                error = target - prediction
                self.weights += self.lr * error * xi
                self.bias += self.lr * error


#2-bit
inputs_2 = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
outputs_2 = np.array([0, 0, 0, 1])

perceptron_2bit = Perceptron(input_size=2)
perceptron_2bit.train(inputs_2, outputs_2)

print("=== 2-Bit AND Gate ===")
print(f"Learned Weights: {perceptron_2bit.weights}")
print(f"Learned Bias: {perceptron_2bit.bias:.2f}\n")

print("Predictions:")
for x in inputs_2:
    print(f"AND{tuple(x)} = {perceptron_2bit.predict(x)}")


#3-bit implementation
inputs_3 = np.array([
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1]
])
outputs_3 = np.array([0, 0, 0, 0, 0, 0, 0, 1])

perceptron_3bit = Perceptron(input_size=3)
perceptron_3bit.train(inputs_3, outputs_3)

print("\n=== 3-Bit AND Gate ===")
print(f"Learned Weights: {perceptron_3bit.weights}")
print(f"Learned Bias: {perceptron_3bit.bias:.2f}\n")

print("Predictions:")
for x in inputs_3:
    print(f"AND{tuple(x)} = {perceptron_3bit.predict(x)}")