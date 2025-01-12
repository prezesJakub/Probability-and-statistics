import numpy


class MultinomialNaiveBayesClassifier:
    def fit(self, X, y):
        self.classes = numpy.unique(y)
        self.feature_probs = {}
        self.class_probs = {}

        for cls in self.classes:
            X_cls = X[y == cls]
            self.class_probs[cls] = len(X_cls) / len(y)
            self.feature_probs[cls] = (X_cls.apply(lambda x: x.value_counts(), axis=0).fillna(0) + 1)

    def predict(self, X):
        predictions = []
        for _, row in X.iterrows():
            probs = {}
            for cls in self.classes:
                probs[cls] = numpy.log(self.class_probs[cls]) + \
                             sum([numpy.log(self.feature_probs[cls][col].get(row[col], 1))
                                  for col in X.columns])
            predictions.append(max(probs, key=probs.get))
        return predictions

    def predict_proba(self, X):
        probas = []
        for _, row in X.iterrows():
            class_probs = {}
            total_prob = 0
            for cls in self.classes:
                log_prob = numpy.log(self.class_probs[cls]) + \
                           sum([numpy.log(self.feature_probs[cls][col].get(row[col], 1))
                                for col in X.columns])
                class_probs[cls] = numpy.exp(log_prob)
                total_prob += class_probs[cls]

            for cls in self.classes:
                class_probs[cls] /= total_prob

            probas.append(class_probs)
        return probas
