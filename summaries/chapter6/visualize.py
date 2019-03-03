import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_style('darkgrid')

df = pd.read_csv('./cache.csv', header=None)
x = range(2, 16)

fig, ax = plt.subplots()
ax.scatter(
    x=x,
    y=df[0],
    label='Process 0'
)
ax.set_yscale('log')
ax.set_xticks(range(2, 16, 2))
ax.set_xlabel('Memory size: $2^x$ [KB]')
ax.set_ylabel('log(access time) [ns/access]')
ax.legend(loc='best')
ax.set_title('Data access time for each data size')
plt.savefig('./data-access-time.png')