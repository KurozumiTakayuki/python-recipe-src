import numpy as np

e1 = np.array([1, 0, 0])
e2 = np.array([0, 1, 0])
e3 = np.cross(e1, e2)
print(e3)
