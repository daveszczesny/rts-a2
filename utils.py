import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def convert_to_csv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            csv_line = ','.join(line.split('\t'))
            outfile.write(csv_line)


def calc_stats(file):
    df = pd.read_csv(file)
    stats  = {}
    for col in df.columns:
        stats[col] = {
            'mean': np.mean(df[col]),
            'std': np.std(df[col]),
            'min': np.min(df[col]),
            'max': np.max(df[col])
        }
    print(stats)
    return stats

def save_stats(stats, file):
    stats_df = pd.DataFrame(stats).T
    stats_df = stats_df.transpose()
    stats_df.to_csv(file, index_label='Column')

def plot_stats(stats, file):
    stats_df = pd.DataFrame(stats).T
    stats_df.plot(kind='bar', figsize=(10, 6), colormap='tab20')
    plt.title('Benchmark Results for Memory Locked Usleep Jitter')
    plt.ylabel('Values')
    plt.xlabel('Statistics')
    plt.xticks(rotation=25, ha='right', fontsize=10)
    plt.legend(title='Columns', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(file)
    plt.show()


name = 'ml_usleep_jitter'

input_file = f'{name}.txt'
output_file = f'{name}.csv'

convert_to_csv(input_file, output_file)
stats = calc_stats(output_file)

save_stats(stats, f'{name}_stats.csv')
plot_stats(stats, f'{name}_stats.png')