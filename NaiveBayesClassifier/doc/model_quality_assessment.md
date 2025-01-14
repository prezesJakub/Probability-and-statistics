## Ocena jakości modelu

### Metodyka

1. **Podział danych**: Dane zostały podzielone na część treningową (70%) i testową (30%).

2. **Trening modelu**: Użyto zaimplementowanych w Pythonie naiwnych klasyfikatów Bayesowskich
   - **Multinomial Naive Bayes** dla zbioru Mushroom (grzyby), który dobrze sprawdza się w przypadku danych kategorycznych.
   - **Gaussian Naive Bayes** dla zbioru Iris (kwiaty), który zakłada, że dane są rozkładami normalnymi.
3. **Metryki oceny**: Ocena jakości modeli opierała się na klasycznych miarach: precision, recall, f1-score i accuracy. Te miary zostały obliczone dla każdej z klas.

#### Raport klasyfikacji dla zbioru Mushroom: 
|               | precision |  recall   | f1-score  | support   |
|---------------|-----------|-----------|-----------|-----------|
|     jadalne   | 0.90      |  1.00     |  0.95     |  1275     |
|  niejadalne   | 1.00      |  0.88     |  0.94     |  1163     |
|    accuracy   |           |           |  0.94     |  2438     |
|   macro avg   | 0.95      |  0.94     |  0.94     |  2438     |
|weighted avg   | 0.95      |  0.94     |  0.94     |  2438     |


#### Raport klasyfikacji dla zbioru Iris: 
|               | precision |  recall   | f1-score  | support   |
|---------------|-----------|-----------|-----------|-----------|
|  setosa       | 1.00      |  1.00     |  1.00     |  17       |
|  versicolor   | 1.00      |  0.89     |  0.94     |  18       |
|   virginica   | 0.83      |  1.00     |  0.91     |  10       |
|    accuracy   |           |           |  0.96     |  45       |
|   macro avg   | 0.94      |  0.96     |  0.95     |  45       |
|weighted avg   | 0.96      |  0.96     |  0.96     |  45       |

## Podsumowanie wyników
Modele osiągnęły bardzo dobrą skuteczność na obu zbiorach danych:
- **Zbiór Mushroom**: Model osiągnął dokładność 94%, z porównywalnym rozkładem między grzybami jadalnymi i niejadalnymi.
- **Zbiór Iris**: Model uzyskał dokładność 96%, z najwyższą dokładnością w przypadku klasy setosa i nieco niższą dla klasy virginica i versicolor.

## Analiza wyników
- **Zbiór Mushroom**: Model osiągnął wysoką dokładność i dobrze różnicuje między klasami "jadalne" i "niejadalne". Wysokie wartości precision i recall wskazują na niewielką liczbę błędów w klasyfikacji.
- **Zbiór Iris**: Model radzi sobie doskonale z klasyfikacją klasy setosa, ale nieco gorzej z pozostałymi klasami. Może mieć to związek z dużo mniejszą próbką danych w przypadku zbioru Iris.

## Wnioski
Modele Naiwnego Klasyfikatora Bayesowskiego osiągnęły wysoką skuteczność w klasyfikacji obu zbiorów. Model Multinomial Naive Bayes dla zbioru Mushroom uzyskał dokładność 94%, skutecznie rozróżniając klasy "jadalne" i "niejadalne". Model Gaussian Naive Bayes dla zbioru Iris osiągnął dokładność 96%, z najlepszymi wynikami dla klasy setosa, ale z nieco gorszą klasyfikacją klas versicolor i virginica.