```python
import numpy as np

sobelX = np.array(
    [[1,0,-1],
     [2,0,-2],
     [1,0,-1],
    ],
    dtype=np.float32,
)


np.pad(sobelX, ((1,1), (1,1)), "constant")
array([[ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  1.,  0., -1.,  0.],
       [ 0.,  2.,  0., -2.,  0.],
       [ 0.,  1.,  0., -1.,  0.],
       [ 0.,  0.,  0.,  0.,  0.]], dtype=float32)


np.pad(sobelX, ((1,1), (1,1)), "constant", constant_values=-100)
array([[-100., -100., -100., -100., -100.],
       [-100.,    1.,    0.,   -1., -100.],
       [-100.,    2.,    0.,   -2., -100.],
       [-100.,    1.,    0.,   -1., -100.],
       [-100., -100., -100., -100., -100.]], dtype=float32)


np.pad(sobelX, ((1,1), (1,1)), "constant", constant_values=(3.14159, 2.71828))
array([[ 3.14159,  3.14159,  3.14159,  3.14159,  2.71828],
       [ 3.14159,  1.     ,  0.     , -1.     ,  2.71828],
       [ 3.14159,  2.     ,  0.     , -2.     ,  2.71828],
       [ 3.14159,  1.     ,  0.     , -1.     ,  2.71828],
       [ 3.14159,  2.71828,  2.71828,  2.71828,  2.71828]], dtype=float32)


#np.pad(sobelX, ((1,1), (1,1)), "constant", constant_values=(3.14159, 2.71828, 777, 42))
ValueError: operands could not be broadcast together with remapped shapes [original->remapped]: (4,) and requested shape (2,2)


np.pad(sobelX, ((1,1), (1,1)), "constant", constant_values=((3.14159, 2.71828), (777, 42)))
array([[777.     ,   3.14159,   3.14159,   3.14159,  42.     ],
       [777.     ,   1.     ,   0.     ,  -1.     ,  42.     ],
       [777.     ,   2.     ,   0.     ,  -2.     ,  42.     ],
       [777.     ,   1.     ,   0.     ,  -1.     ,  42.     ],
       [777.     ,   2.71828,   2.71828,   2.71828,  42.     ]],
      dtype=float32)

```

