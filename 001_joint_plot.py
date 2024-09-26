import matplotlib.pyplot as plt
import seaborn as sns


def plot_jointplot(data, x_col, y_col, kind='scatter'):
    sns.jointplot(x=x_col, y=y_col, data=data, kind=kind)
    plt.show()


# Usage
data = sns.load_dataset("iris")
plot_jointplot(data, "sepal_length", "sepal_width", "hex")
