import argparse
import pandas as pd
import argparse
from scipy import stats
import matplotlib.pyplot as plt
import os


# Constants.
BINS = ['Not detected ramp', 'Low ramp', 'Medium ramp', 'High ramp', 'Not detected no ramp', 'Low no ramp', 'Medium no ramp', 'High no ramp']
EXPRESSION_BINS = ['Not detected', 'Low', 'Medium', 'High']
RAMP_BINS = ['ramp', 'no ramp']

def parse_args():
    ''' Parse arguments. '''
    parser = argparse.ArgumentParser(description='Run Shapiro-Wilk tests on expression data and generate histograms.')
    parser.add_argument('-i', '--input', help='path to rampCountPerTissueByGeneExpression CSVs.', nargs='*', action='store', dest='input', required=True)
    parser.add_argument('-o', '--output', help='The directory to which output files will be saved.', type=str, default='.', required=False)
    args = parser.parse_args()
    return args


def run_shapiro_wilk(df):
    '''
    Run a Shapiro-Wilk test for each bin.
    '''
    results = {}
    for bin in BINS:
        s,p = stats.shapiro(df[bin].values)
        results[bin] = [s,p]

    results_df = pd.DataFrame.from_dict(results, orient='index', columns=['Statistic', 'P-value'])
    results_df['Expression/Ramp Bin'] = results_df.index
    results_df[['Expression/Ramp Bin', 'Statistic', 'P-value']]
    results_df['P-value'] = results_df['P-value'].apply(lambda x: '%.8f' % x)

    return results_df


def plot_histograms(df, out_dir, file_name_wo_ext):
    '''
    Plot a histrogram of the number of genes that each tissue has in each bin.
    '''

    plot_dir = 'histograms_' + file_name_wo_ext
    os.mkdir(f'{out_dir}/{plot_dir}')

    for exp in EXPRESSION_BINS:
        for r in RAMP_BINS:

            col = exp + ' ' + r

            plt.clf()
            plt.hist(df[col].values, bins=20, edgecolor='black')
            plt.suptitle(f'Expression = {exp}', fontsize=14)
            plt.title(r, fontsize=12)
            plt.ylabel('Tissue Count')
            plt.xlabel('Number of Genes')

            plot_file_name = col.replace(' ', '_')
            plt.savefig(f'{out_dir}/{plot_dir}/{plot_file_name}.png')


if __name__ == '__main__':
    ''' Main. '''
    args = parse_args()
    out_dir = args.output.rstrip('/')
    input_files = args.input
    
    for file_name in input_files:

        df = pd.read_csv(file_name)
        file_name_wo_ext = file_name.rsplit('.')[0].rsplit('/')[-1]

        results_df = run_shapiro_wilk(df)
        results_df.to_csv(f'{out_dir}/shapiro_wilk_results_{file_name_wo_ext}.csv', index=False)

        plot_histograms(df, out_dir, file_name_wo_ext)
