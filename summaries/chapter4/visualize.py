import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_style('darkgrid')

filenames = [
    '1core-1process',
    '1core-2process',
    '1core-4process',
    '2core-1process',
    '2core-2process',
    '2core-4process',
    'nice-1core-2process'
]

for filename in filenames:
    df = pd.read_csv('./' + filename + '.tsv', sep='\t', header=None)

    fig, ax = plt.subplots()
    processes = sorted(df[0].unique())
    for process in processes:
        ax.scatter(x=df[df[0] == process][1], y=df[df[0] == process][0], label='Process {0}'.format(process))
    ax.set_yticks(range(0, 4, 1))
    ax.set_xlabel('Elapsed time [ms]')
    ax.set_ylabel('Process ID')
    ax.set_title('The processes running on a logical CPU')
    plt.savefig('./' + filename + '-processes.png')

    fig, ax = plt.subplots()
    for process in processes:
        ax.scatter(x=df[df[0] == process][1], y=df[df[0] == process][2], label='Process {0}'.format(process))
    ax.set_ylim(0, 100)
    ax.set_xlabel('Elapsed time [ms]')
    ax.set_ylabel('The progress [%]')
    ax.set_title('The progress per each process')
    ax.legend(loc='best')
    plt.savefig('./' + filename + '-progress.png')