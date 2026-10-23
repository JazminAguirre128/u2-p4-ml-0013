import pandas as pd
import numpy as np
# Meredith Aguirre NC = 0013 Fecha 23/10/2026

n_filas = 5
n_columnas = 5
tag_columna = tuple('ABCDE') #  Etiquetas para las columnas de una tupla
print(tag_columna)
matriz = np.random.randint(1, 7, size = (n_filas, n_columnas))
print("Genera matriz de 5 filas por 5 columnas")
print("Con numeros aleatorios comprimidos entre 1 y 10")
print(matriz)
# La variable df es DataFrame
df = pd.DataFrame(matriz, columns = tag_columna)
print("-------- La tabla o DataFrame -------- NC = 0013")
print(df)
print("Meredith Aguirre NC = 0013 Fecha 23/10/2026")