import numpy


class GaussianNaiveBayesClassifier:
    def fit(self, X, y):
        self.classes = numpy.unique(y)
        self.class_probs = {}
        self.feature_means = {}
        self.feature_variances = {}

        for cls in self.classes:
            X_cls = X[y == cls]
            self.class_probs[cls] = len(X_cls) / len(y)
            self.feature_means[cls] = X_cls.mean(axis=0)
            self.feature_variances[cls] = X_cls.var(axis=0)

    def predict(self, X):
        predictions = []
        for _, row in X.iterrows():
            probs = {}
            for cls in self.classes:
                prob = numpy.log(self.class_probs[cls])
                for i, feature in enumerate(X.columns):
                    mean = self.feature_means[cls][i]
                    var = self.feature_variances[cls][i]
                    prob += self.log_normal_distribution(row[feature], mean, var)
                probs[cls] = prob
            predictions.append(max(probs, key=probs.get))
        return predictions

    def predict_proba(self, X):
        probas = []
        for _, row in X.iterrows():
            class_probs = {}
            total_prob = 0
            for cls in self.classes:
                log_prob = numpy.log(self.class_probs[cls])
                for i, feature in enumerate(X.columns):
                    mean = self.feature_means[cls][i]
                    var = self.feature_variances[cls][i]
                    log_prob += self.log_normal_distribution(row[feature], mean, var)
                class_probs[cls] = numpy.exp(log_prob)
                total_prob += class_probs[cls]

            for cls in self.classes:
                class_probs[cls] /= total_prob

            probas.append(class_probs)
        return probas

    def log_normal_distribution(self, x, mean, var):
        exponent = numpy.exp(-0.5 * ((x-mean) ** 2) / var)
        return numpy.log((1 / numpy.sqrt(2 * numpy.pi * var)) * exponent)