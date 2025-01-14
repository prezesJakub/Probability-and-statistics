# Wstępna analiza danych

W niniejszym dokumencie przedstawiona jest wstępna analiza danych dla dwóch zbiorów danych: **Mushroom** oraz **Iris**. Analiza obejmuje identyfikację brakujących wartości, proporcje klas oraz rozkład cech z wykorzystaniem wykresów wygenerowanych wcześniej w Pythonie przy zastosowaniu biblioteki _matplotlib_.

---

## 1. Zbiór Mushroom

### Opis zbioru danych

Zbiór Mushroom zawiera informacje o grzybach, które klasyfikowane są na dwie klasy: **jadalne** lub **trujące**. Dane te zawierają różne cechy grzybów, takie jak kolor kapelusza, kolor łodygi, kształt, zapach, itp.

### Analiza brakujących wartości

```python
missing_values = mushroom_data.isnull().sum()
print("Brakujące wartości w kolumnach: ")
print(missing_values)
return missing_values
```

Przy pomocy powyższego kodu, sprawdzono, że dane nie zawierają braków.

### Proporcja klas

![Proporcja klas - Mushroom](../plots/Mushroom/jadalność_distribution.png)

Powyższy wykres przedstawia ilość grzybów danej klasy.

### Rozkład cech

![Rozkład cechy cap-shape](../plots/Mushroom/cap-shape_distribution.png)

![Rozkład cechy cap-surface](../plots/Mushroom/cap-surface_distribution.png)

![Rozkład cechy cap-color](../plots/Mushroom/cap-color_distribution.png)

![Rozkład cechy bruises](../plots/Mushroom/bruises_distribution.png)

![Rozkład cechy odor](../plots/Mushroom/odor_distribution.png)

![Rozkład cechy gill-attachment](../plots/Mushroom/gill-attachment_distribution.png)

![Rozkład cechy gill-spacing](../plots/Mushroom/gill-spacing_distribution.png)

![Rozkład cechy gill-size](../plots/Mushroom/gill-size_distribution.png)

![Rozkład cechy gill-color](../plots/Mushroom/gill-color_distribution.png)

![Rozkład cechy stalk-shape](../plots/Mushroom/stalk-shape_distribution.png)

![Rozkład cechy stalk-root](../plots/Mushroom/stalk-root_distribution.png)

![Rozkład cechy stalk-surface-above-ring](../plots/Mushroom/stalk-surface-above-ring_distribution.png)

![Rozkład cechy stalk-surface-below-ring](../plots/Mushroom/stalk-surface-below-ring_distribution.png)

![Rozkład cechy stalk-color-above-ring](../plots/Mushroom/stalk-color-above-ring_distribution.png)

![Rozkład cechy stalk-color-below-ring](../plots/Mushroom/stalk-color-below-ring_distribution.png)

![Rozkład cechy veil-type](../plots/Mushroom/veil-type_distribution.png)

![Rozkład cechy veil-color](../plots/Mushroom/veil-color_distribution.png)

![Rozkład cechy ring-number](../plots/Mushroom/ring-number_distribution.png)

![Rozkład cechy ring-type](../plots/Mushroom/ring-type_distribution.png)

![Rozkład cechy spore-print-color](../plots/Mushroom/spore-print-color_distribution.png)

![Rozkład cechy population](../plots/Mushroom/population_distribution.png)

![Rozkład cechy habitat](../plots/Mushroom/habitat_distribution.png)

Powyższe wykresy przedstawiają rozkład ilościowy poszczególnych cech.

Na podstawie analizy wykresów możemy zauważyć, że szczególnie istotne w ocenie przynależności danego grzyba do klas są między innymi cechy: *_bruises_*, *_odor_*, *_gill-color_*, *_stalk-surface-above-ring_*, *_ring-type_*, *_spore-point-color_*,*_population_*.

Wśród podanych cech, możemy zauważyć częściej wyraźne wskazanie na klasę grzyba na podstawie wartości danej cechy.

Następujące wartości wśród cech determinują ze stuprocentowym prawdopodobieństwem klasę danego grzyba:

**cap-color**:
u 100% jadalne
r 100% jadalne
**cap-shape**:
s 100% jadalne
c 100% trujące
**cap-surface**:
g 100% trujące
**gill-color**:
e 100% jadalne
b 100% trujące
r 100% trujące
o 100% jadalne
**habitat**:
w 100% jadalne
**odor**:
p 100% trujące
a 100% jadalne
l 100% jadalne
c 100% trujące
y 100% trujące
s 100% trujące
m 100% trujące
**population**:
n 100% jadalne
a 100% jadalne
**ring-numer**:
n 100% trujące
**ring-type**:
f 100% jadalne
n 100% trujące
**spore-print-color**:
u 100% jadalne
r 100% trujące
o 100% jadalne
y 100% jadalne
b 100% jadalne
**stalk-color-above-ring_distribution**:
g 100% jadalne
b 100% trujące
e 100% jadalne
o 100% jadalne
c 100% trujące
y 100% trujące
**stalk-color-below-ring_distribution**:
e 100% jadalne
y 100% trujące
o 100% jadalne
c 100% trujące
**stalk-root_distribution**:
r 100% jadalne
**veil-color_distribution**:
n 100% jadalne
o 100% jadalne
y 100% trujące

## 2. Zbiór Iris

### Analiza brakujących wartości

```python
missing_values = iris_data.isnull().sum()
print("Brakujące wartości w kolumnach: ")
print(missing_values)
return missing_values
```

Przy pomocy powyższego kodu, sprawdzono, że dane nie zawierają braków.

### Proporcja klas

![Proporcja klas - Iris](../plots/Iris/iris_class_proportion.png)

Powyższy wykres przedstawia ilość irysów danego gatunku.

### Rozkład cech

![Rozkład cechy petal length (cm)](../plots/Iris//petal%20length%20(cm)_distribution.png)

![Rozkład cechy petal width (cm)](../plots/Iris//petal%20width%20(cm)_distribution.png)

![Rozkład cechy sepal length (cm)](../plots/Iris//sepal%20length%20(cm)_distribution.png)

![Rozkład cechy sepal width (cm)](../plots/Iris//sepal%20width%20(cm)_distribution.png)

Powyższe wykresy przedstawiają rozkłady wartości poszczególnych cech irysów.

Na podstawie analizy powyższych histogramów, możemy stwierdzić, iż szczególnie istotne dla oceny przynależności danego kwiatu są cechy _*petal length*_ i _*petal width*_, gdyż wartości dla gatunku _*setosa*_ są wyraźnie odseparowane od gatunków _*versicolor*_ i _*virginica*_.

Wyraźne wzorce sugerujące podziały na gatunki występują dla klasy _*setosa*_. Wartości tej klasy wyróżniają się na tle innych klas, co sprawia, że klasa ta jest najłatwiejsza do sklasyfikowania.