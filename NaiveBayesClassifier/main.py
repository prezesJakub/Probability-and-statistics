from data_processing import load_mushroom_data, load_iris_data, split_data
from multinomial_naive_bayes import MultinomialNaiveBayesClassifier
from gaussian_naive_bayes import GaussianNaiveBayesClassifier
from sklearn.metrics import classification_report


def main():
    mushroom_data = load_mushroom_data()

    mushroom_data['target'] = mushroom_data['class'].map({'e': 0, 'p': 1})
    X = mushroom_data.drop(columns=['class', 'target'])
    y = mushroom_data['target']

    X_train, X_test, y_train, y_test = split_data(mushroom_data, target_column='target')

    model = MultinomialNaiveBayesClassifier()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    probs = model.predict_proba(X_test)

    mushroom_accuracy = sum(predictions == y_test) / len(y_test)

    iris_data = load_iris_data()

    A = iris_data.drop(columns=['target'])
    b = iris_data['target']
    A_train, A_test, b_train, b_test = split_data(iris_data, target_column='target')

    iris_model = GaussianNaiveBayesClassifier()
    iris_model.fit(A_train, b_train)

    iris_predictions = iris_model.predict(A_test)
    iris_probs = iris_model.predict_proba(A_test)

    iris_accuracy = sum(iris_predictions == b_test) / len(b_test)

    print("Zbiór mushroom:")
    print(f"Dokładność klasyfikatora wyniosła: {mushroom_accuracy:.2%}")

    for i in range(len(probs)):
        print(f"\nPrawdopodobieństwa dla przykładu nr {i}:")
        for cls, prob in probs[i].items():
            print(f"Klasa {cls}: {prob:.4f}")

    print("\nRaport klasyfikacji: ")
    print(classification_report(y_test, predictions))

    print("Zbiór iris:")
    print(f"Dokładność klasyfikatora wyniosła: {iris_accuracy:.2%}")

    for i in range(len(iris_probs)):
        print(f"\nPrawdopodobieństwa dla przykładu nr {i}:")
        for cls, prob in iris_probs[i].items():
            print(f"Klasa {cls}: {prob:.4f}")

    print("\nRaport klasyfikacji: ")
    print(classification_report(b_test, iris_predictions))


if __name__ == "__main__":
    main()
