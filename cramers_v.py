import argparse
import pandas as pd

# Constants.
CRAMERS_V = 'Cramers V'
CHI_SQ = 'Chi sq'
TOTAL_GENES = 'Total genes'
K = 2

def parse_args():
    ''' Parse arguments. '''
    parser = argparse.ArgumentParser(description='Compute Cramer\'s V for tissue/cell-type ramp/expression counts Chi-square test results.')
    parser.add_argument('-i', '--input', help='path to rampCountPerTissueByGeneExpression CSVs.', nargs='*', action='store', dest='input', required=True)
    parser.add_argument('-o', '--output', help='The directory to which output files will be saved.', type=str, default='.', required=False)
    args = parser.parse_args()
    return args

def cramers_v(chi, n, k):
    ''' Compute Cramer's V. '''
    v = (chi / (n * (k - 1))) ** 0.5
    return v

if __name__ == '__main__':
    ''' Main. '''
    args = parse_args()
    out_dir = args.output.rstrip('/')
    input_files = args.input

    for file_name in input_files:

        df = pd.read_csv(file_name)
        file_name_wo_ext = file_name.rsplit('.')[0].rsplit('/')[-1]
        df[CRAMERS_V] = df.apply(lambda row: cramers_v(row[CHI_SQ], row[TOTAL_GENES], K), axis=1)
        df.to_csv(f'{file_name_wo_ext}.csv', index=False)