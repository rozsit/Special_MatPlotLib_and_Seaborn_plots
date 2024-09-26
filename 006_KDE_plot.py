import matplotlib.pyplot as plt
import seaborn as sns


def plot_kde(data, column):
    sns.kdeplot(data[column], shade=True)
    plt.show()


# Usage
data = sns.load_dataset("iris")

plot_kde(data, "sepal_length")
