import pandas as pd
import numpy as np
import seaborn as sns

running_pos = 0
cumulative_pos = []

df = pd.read_csv('txtForManhattan_tissue.txt', sep='\t')
df['-logp'] = - np.log(df['p-value'])
for chromosome, group_df in df.groupby('chrom'):
	cumulative_pos.append(group_df['cdsStart'] + running_pos)
	running_pos += group_df['cdsStart'].max()
	
df['cumulative_pos'] = pd.concat(cumulative_pos)
df['SNP number'] = df.index

manhattan_plot = sns.relplot(
	data = df.sample(10456),
	x = 'cdsStart',
	y = '-logp',
	aspect = 4,
	hue = 'chrom',
	palette = 'Set1',
	linewidth=0,
	s = 6,
	legend = None
	
)
manhattan_plot.ax.set_xlabel("Chromosome")
manhattan_plot.ax.set_xticks(df.groupby('chrom')['cdsStart'].median())
##manhattan_plot.ax.set_xticklabels([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,'X','Y'])
manhattan_plot.ax.set_xticklabels(df['chrom'].unique())
manhattan_plot.fig.suptitle('Ramps in Tissues')
manhattan_plot.savefig("manhattan_tissue.png")


