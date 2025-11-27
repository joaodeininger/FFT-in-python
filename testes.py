import numpy as np

# funcao complex(a,b) recebe parte real e parte imaginaria e cria numero complexo com base nesses dois valores

data = np.loadtxt("entrada2.txt")
complex_array = np.array(data, dtype=complex)
print(complex_array)

