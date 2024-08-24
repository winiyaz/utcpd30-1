# Actual work - hints.py is just hints
import pandas as pd

# Detup Data Frame
da = pd.read_csv("np.csv")

# Dictionary comprehension
dic = {row.letter: row.code for (index, row) in da.iterrows()}
print(dic)


def ge_po():
	# Getting input
	wo = input("WriteWord: ").upper()
	try:
		out = [dic[letter] for letter in wo]
	except KeyError:
		print(f"""
	Entered : {wo}
	!! Letters from alphabhet only !!
	""")
		ge_po()
	else:
		print(out)


ge_po()
