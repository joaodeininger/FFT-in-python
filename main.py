# import numpy as np
import pandas as pd

df = pd.read_csv("entrada.txt", sep=" ", header=None, names=["real", "imag"])

df = df.replace("", float("nan"))
df = df.fillna(0.0)

df["real"] = pd.to_numeric(df["real"], errors="coerce").fillna(0.0)
df["imag"] = pd.to_numeric(df["imag"], errors="coerce").fillna(0.0)

df["complexo"] = df["real"] + 1j * df["imag"]


print("\n--- Resultado da Entrada ---")
