import numpy as np

arr = np.random.randint(1, 51, (3, 4))
print(arr)
print("Mean:", arr.mean())
print("Median:", np.median(arr))
print("Std:", arr.std())
print("Sum:", arr.sum())
print("Row Sum:", arr.sum(axis=1))
print("Reshaped:\n", arr.reshape(2, 6))