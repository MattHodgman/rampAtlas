import sys
import numpy as np
import pandas as pd

df = pd.read_csv('txtForManhattan_tissue.txt', sep = "\t")
df['-logp'] = -np.log(df['p-value'])
