import pandas
import seaborn
import matplotlib.pyplot as plt
from data_processing import load_mushroom_data


def analyze_missing_values():
    missing_values = mushroom_data.isnull().sum()
    print("Brakujące wartości w kolumnach: ")
    print(missing_values)
    return missing_values

def analyze_class_proportion():
    print("Proporcja grzybów jadalnych i trujących:")
    mushroom_data['class_label'] = mushroom_data['class'].map({'e': 'jadalne', 'p': 'trujące'})
    value_counts = mushroom_data['class_label'].value_counts()
    print(value_counts)

    ax = value_counts.plot(kind='bar', title='Proporcja grzybów')
    ax.set_xticklabels(['jadalne', 'trujące'], rotation=0)

    for i, value in enumerate(value_counts):
        ax.text(i, value + 5, str(value), ha='center', va='bottom', fontsize=10)

    plt.ylabel("Liczba wystąpień")
    plt.xlabel("Rodzaj grzyba")
    plt.show()

def analyze_feature_distribution(draw_plots=False):
    print("Analiza wartości rozkładu cech")
    for column in mushroom_data.columns:
        print(f"\nRozkład wartości cechy: {column}")
        print(mushroom_data[column].value_counts())
        if draw_plots:
            plt.figure()
            value_counts = mushroom_data[column].value_counts()
            ax = value_counts.plot(kind='bar', title=f"Rozkład wartości cechy: {column}")
            ax.set_ylabel("Liczba wystąpień")
            ax.set_xlabel("Rodzaj cechy")
            ax.set_xticklabels(ax.get_xticklabels(), rotation=0)

            for i, value in enumerate(value_counts):
                ax.text(i, value + 5, str(value), ha='center', va='bottom', fontsize=10)
    if draw_plots:
        plt.show()

def analyze_feature_importance(draw_plots=False):
    mushroom_data['jadalność'] = mushroom_data['class'].map({'e': 'jadalne', 'p': 'trujące'})

    categorical_columns = mushroom_data.select_dtypes(include=['object']).columns

    for column in categorical_columns:
        if draw_plots:
            plt.figure()
            ax = seaborn.countplot(x=column, hue='jadalność', data=mushroom_data)
            plt.title(f'Porównanie rozkładu cechy: {column}')
            plt.xlabel(f'Wartości cechy: {column}')
            plt.ylabel('Liczba wystąpień')
            plt.xticks(rotation=0)

            for p in ax.patches:
                height = p.get_height()
                if height > 0:
                    ax.text(p.get_x() + p.get_width() / 2, height + 0.1, int(height), ha='center', va='bottom',
                            fontsize=10)

    plt.show()

if __name__ == "__main__":
    mushroom_data = load_mushroom_data()
   # analyze_missing_values()
   # analyze_class_proportion()
   # analyze_feature_distribution(True)
   # analyze_feature_importance(True)