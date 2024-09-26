import matplotlib.pyplot as plt
import seaborn as sns


def plot_ridge(data, x_col, category_col):
    g = sns.FacetGrid(data, row=category_col, hue=category_col, aspect=5)
    g.map(sns.kdeplot, x_col, clip_on=False,
          fill=True, alpha=1, lw=1.5, bw_method=0.2)
    g.map(sns.kdeplot, x_col, clip_on=False,
          color="w", lw=1, bw_method=0.2)
    g.map(plt.axhline, y=0, lw=2, clip_on=False)
    plt.show()


# Usage
data = sns.load_dataset("diamonds")
subset_data = data[data['cut'].isin(['Ideal', 'Fair', 'Good'])]

plot_ridge(subset_data, "price", "cut")
