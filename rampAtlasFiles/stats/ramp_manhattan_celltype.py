import pandas as pd
import numpy as np
import seaborn as sns

running_pos = 0
cumulative_pos = []

df = pd.read_csv('txtForManhattan_celltype.txt', sep='\t')
df['-logp'] = - np.log(df['p-value'])
for chromosome, group_df in df.groupby('chrom'):
	cumulative_pos.append(group_df['cdsStart'] + running_pos)
	running_pos += group_df['cdsStart'].max()
	
df['cumulative_pos'] = pd.concat(cumulative_pos)
df['SNP number'] = df.index

sns_plot = sns.relplot(
	data = df.sample(10456),
	x = 'cumulative_pos',
	y = '-logp',
	aspect = 4,
	hue = 'chrom',
	palette = 'Set1'
)

sns_plot.savefig("manhattan_celltype.png")


