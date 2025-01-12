import pandas
import seaborn
import matplotlib.pyplot as plt
from data_processing import load_iris_data


def analyze_missing_values():
    missing_values = iris_data.isnull().sum()
    print("Brakujące wartości w kolumnach: ")
    print(missing_values)
    return missing_values

def analyze_class_proportion():
    print("Proporcja gatunków Iris:")
    value_counts = iris_data['target'].value_counts()
    print(value_counts)

    ax = value_counts.plot(kind='bar', title='Proporcja gatunków Iris')
    ax.set_xticklabels(value_counts.index, rotation=0)

    for i, value in enumerate(value_counts):
        ax.text(i, value + 0.2, str(value), ha='center', va='bottom', fontsize=10)

    plt.ylabel("Liczba wystąpień")
    plt.xlabel("Rodzaj gatunku")
    plt.savefig(f'plots/iris_class_proportion.png')
    plt.close()

    plt.show()

def analyze_feature_distribution(draw_plots=False):
    print("Analiza wartości rozkładu cech")
    for column in iris_data.columns:
        print(f"\nRozkład wartości cechy: {column}")
        print(iris_data[column].describe())
        if draw_plots:
            plt.figure()
            seaborn.histplot(iris_data[column], kde=True, bins=15)
            plt.title(f"Rozkład wartości cechy: {column}")
            plt.xlabel(f"Wartości cechy: {column}")
            plt.ylabel('Liczba wystąpień')

    if draw_plots:
        plt.show()

def analyze_feature_importance(draw_plots=False):
    numerical_columns = iris_data.select_dtypes(include=['float64', 'int64']).columns

    for column in numerical_columns:
        if draw_plots:
            plt.figure()
            seaborn.boxplot(x='target', y=column, data=iris_data)
            plt.title(f'Porównanie rozkładu cechy: {column}')
            plt.xlabel(f'Rodzaj gatunku')
            plt.ylabel(f'Wartości cechy: {column}')
            plt.xticks(rotation=0)

    if draw_plots:
        plt.show()

if __name__ == "__main__":
    iris_data = load_iris_data()
   # analyze_missing_values()
   # analyze_class_proportion()
   # analyze_feature_distribution(True)
   # analyze_feature_importance(True)