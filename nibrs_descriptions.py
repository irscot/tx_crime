import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("houston_crime.csv", dtype=str)

print(df["NIBRS Description"].unique())