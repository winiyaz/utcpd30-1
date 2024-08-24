# Actual work - hints.py is just hints
import pandas as pd

# Detup Data Frame
da = pd.read_csv("np.csv")

# Dictionary comprehension
dic = {row.letter: row.code for (index, row) in da.iterrows()}
print(dic)

# Getting input
wo = input("WriteWord: ").upper()
out = [dic[letter] for letter in wo]
print(out)
