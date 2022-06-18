import numpy as np

# ------------------------
#    TEST EQUALITY
# ------------------------
shape = (512, 6)
randint_low = 0
# should be high enought, otherwise max2_indices and
# m2_ind may not equal in the following: There exist
# more than one way to sort an array with repeated numbers.
randint_high = randint_low + 1_000_000
A = np.random.randint(randint_low, randint_high, size=shape)
max_indices = np.argmax(A, axis=-1)
mask = np.ones(shape, dtype=bool)
mask[range(A.shape[0]), max_indices] = False
A2 = A[mask].reshape(shape[0], shape[1]-1)
tmp_max2_indices = np.argmax(A2, axis=-1)
max2_indices = tmp_max2_indices + (tmp_max2_indices >= max_indices)
sorted_indices = np.argsort(A, axis=-1)
m2_ind = sorted_indices[..., -2]
print("Is max2_indices equal to m2_ind?")
print(np.array_equal(max2_indices, m2_ind))



# -----------------------------
#  TEST COMPLEXITY / EXE TIME
# -----------------------------
shape = (512, 6)
#shape = (512, 17)
randint_low = 0
randint_high = randint_low + 1_000_000
A = np.random.randint(randint_low, randint_high, size=shape)

%%timeit
max_indices = np.argmax(A, axis=-1)
mask = np.ones(shape, dtype=bool)
mask[range(A.shape[0]), max_indices] = False
A2 = A[mask].reshape(shape[0], shape[1]-1)
tmp_max2_indices = np.argmax(A2, axis=-1)
max2_indices = tmp_max2_indices + (tmp_max2_indices >= max_indices)


%%timeit
sorted_indices = np.argsort(A, axis=-1)
m2_ind = sorted_indices[..., -2]
m_ind = sorted_indices[..., -1]
