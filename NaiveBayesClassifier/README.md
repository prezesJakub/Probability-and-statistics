# Projekt: Naiwny klasyfikator Bayesowski

_**Autorzy**: Jakub Zając, Kacper Wdowiak_

## **Opis projektu**
Projekt ten dotyczy implementacji naiwnego klasyfikatora Bayesowskiego oraz analizy jego wydajności na dwóch popularnych zbiorach danych:
- **Mushroom**: klasyfikacja grzybów jako jadalne lub trujące.
- **Iris**: klasyfikacja gatunków irysów.

## **Wymagania systemowe**
Projekt wykorzystuje język Python oraz następujące biblioteki:
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`

Aby zainstalować wszystkie wymagane biblioteki, użyj polecenia:
```bash
pip install -r requirements.txt
```

## **Struktura projektu**

W głównym folderze projektu, znajdują się pliki z implementacją naiwnych klasyfikatorów Bayesowskich oraz pliki generujące wykresy służące do wstępnej analizy danych.

W pliku `data_processing.py` znajduje się kod pobierający zbiory danych Mushroom i Iris oraz metoda dzieląca dany zbiór na część testową i treningową.

W pliku `multinomial_naive_bayes.py` znajduje się implementacja naiwnego klasyfikatora Bayesowskiego wspierającego cechy kategoryczne, takie jak w zbiorze Mushroom.

W pliku `gaussian_naive_bayes.py` znajduje się implementacja naiwnego klasyfikatora Bayesowskiego wspierającego cechy ilościowe, takie jak w zbiorze Iris.

W plikach `mushroom_data_analysis.py` i `iris_data_analysis.py` znajduje się kod generujący wykresy pomocne we wstępnej analizie danych.

W pliku `main.py` testujemy działanie zaimplementowanych naiwnych klasyfikatorów Bayesowskich oraz generujemy dane, będące pomocne w ocenie jakości modelu.

W folderze `plots` znajdują się wygenerowane w Pythonie przy użyciu biblioteki `matplotlib` wykresy przedstawiające rozkład danych cech w zbiorach Mushroom oraz Iris.

W folderze `doc` znajduje się pozostała część dokumentacji: Wstępna analiza danych oraz Ocena jakości modelu.

W folderze `data` znajduje się plik CSV ze zbiorem danych Mushroom. Zbiór danych Iris jest dostępny w bibliotece `scikit-learn`.

## **Opis algorytmu**

Multinomial Naive Bayes Classifier to klasyfikator stosowany głównie dla danych kategorycznych, gdzie cechy reprezentują dyskretne wartości, takie jak liczba wystąpień. Założeniem tego klasyfikatora jest to, że cechy są warunkowo niezależne w obrębie każdej klasy.

Gaussian Naive Bayes Classifier to klasyfikator stosowany głównie dla danych ciągłych. Zakłada on, że wartości cech w każdej klasie rozkładają się zgodnie z rozkładem normalnym. W modelu wykorzystywane są statystyki, takie jak średnia i wariancja każdej cechy w obrębie klasy.

W fazie trenowania modelu, dla każdej z klas wyznaczamy częstości ich wystąpienia oraz częstości wystąpienia poszczególnych wartości cech w danych.

Metoda predict zwraca przewidywaną klasę dla każdego z obiektów. Dla każdego z obiektów obliczane jest prawdopodobieństwo przynależności do klasy na podstawie wartości cech, których prawdopodobieństwo warunkujące klasę zostało wcześniej obliczone. Prawdopodobieństwa są obliczane przy użyciu logarytmów, aby uniknąć problemów z małymi liczbami. 

Metoda predict_proba w podobny sposób oblicza i zwraca prawdopodobieństwa przynależności danego obiektu do każdej z klas.