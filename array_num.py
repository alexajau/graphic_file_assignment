import numpy as np
import random
import math

array = np.random.randint(1, 10, size=(5,5), dtype=int)
print(array)
print(array[1][2])
print("sum = ", sum(map(sum,array)))
print("means = ", np.mean(array, axis=1))
print("maximum numbers = ", np.amax(array, axis=1))