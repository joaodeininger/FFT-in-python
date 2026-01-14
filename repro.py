
import numpy as np
import pandas as pd
import fft as ft
import os

# Create dummy input files if they don't exist, matching the content we saw
os.makedirs("convolution", exist_ok=True)
with open("convolution/xn.txt", "w") as f:
    f.write("2 \n1 \n1 \n2 \n-1 \n1 \n1 \n") # Added trailing spaces to potential simulate issue

with open("convolution/hn.txt", "w") as f:
    f.write("1\n1\n1\n")

print("Loading files...")
# Simulate main.py loading
try:
    x = pd.read_csv("convolution/xn.txt", sep=" ", header=None)
    h = pd.read_csv("convolution/hn.txt", sep=" ", header=None)
except Exception as e:
    # If read_csv fails with sep=" " due to variable cols, try to emulate what might be happening
    # But usually it just produces NaNs
    print(f"Pandas read failed: {e}")
    exit()

print(f"x shape: {x.shape}")
print(f"h shape: {h.shape}")
print("x head:")
print(x.head())

print("Running seccionada...")
try:
    y = ft.seccionada(x, h)
    print("Success")
    print(y)
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
