# Kalkulator Erlanga

Kalkulator Erlanga to aplikacja umożliwiająca wyznaczenie współczynnika blokady w systemach ze stratami zgłoszeń opisanych modelem Erlanga. Program umożliwia obliczanie trzech różnych wartości: natężenia ruchu, współczynnika blokady oraz ilości linii/kanałów w systemie.

## Model Erlanga

Model Erlanga jest wykorzystywany do analizy i modelowania systemów telekomunikacyjnych oraz sieci komputerowych. Model ten opisuje proces obsługi zgłoszeń przychodzących w systemie, uwzględniając intensywność zgłoszeń i liczbę dostępnych linii obsługi. 

<p align="center">

# Interfejs główny
  <img src="https://i.imgur.com/JaoBCuk.png" width="80%" height="80%">

# Generowanie wykresu
  <img src="https://i.imgur.com/5fLOlml.png" width="80%" height="80%">

# Prezentacja wykresu
  <img src="https://i.imgur.com/eZoHl8p.png" width="80%" height="80%">
</p>

## Funkcje kalkulatora

Kalkulator Erlanga udostępnia trzy główne funkcje:

1. **Obliczanie natężenia ruchu**: Pozwala na obliczenie natężenia ruchu w systemie na podstawie liczby linii obsługi i współczynnika blokady. Natężenie ruchu wyraża się w erlangach i odzwierciedla liczbę zgłoszeń przychodzących na jednostkę czasu.

2. **Obliczanie współczynnika blokady**: Pozwala na obliczenie współczynnika blokady, czyli prawdopodobieństwa, że zgłoszenie nie zostanie obsłużone. Do obliczenia współczynnika blokady potrzebne są intensywność zgłoszeń oraz liczba linii obsługi.

3. **Obliczanie ilości linii/kanałów**: Pozwala na obliczenie minimalnej liczby linii/kanałów potrzebnych do osiągnięcia danego współczynnika blokady przy określonym natężeniu ruchu.

## Interfejs graficzny

Aplikacja posiada prosty interfejs graficzny oparty na frameworku Kivy. Interfejs umożliwia wybór trybu obliczeń (natężenie ruchu, współczynnik blokady, ilość linii/kanałów) oraz wprowadzenie odpowiednich wartości wejściowych. Po naciśnięciu przycisku "Oblicz", aplikacja prezentuje wynik obliczeń na ekranie.

## Instrukcja obsługi

1. **Główny ekran**: Na głównym ekranie należy wybrać tryb obliczeń z rozwijanej listy (Natężenie ruchu, Współczynnik blokady, Ilość linii/kanałów). Następnie wprowadzić odpowiednie wartości w polach tekstowych. Po naciśnięciu przycisku "Oblicz", wynik obliczeń pojawi się na ekranie.

2. **Generowanie wykresu**:
Funkcja generowania wykresu współczynnika blokady w kalkulatorze Erlanga umożliwia wizualizację zależności między natężeniem ruchu a współczynnikiem blokady w systemie.

Po wybraniu trybu obliczeń "Współczynnik blokady" na głównym ekranie i wprowadzeniu wartości natężenia ruchu oraz liczby linii obsługi, można nacisnąć przycisk "Oblicz", aby uzyskać wartość współczynnika blokady oraz wygenerować wykres.

Funkcja generowania wykresu działa w następujący sposób:

1. **Pobranie danych wejściowych**: Na podstawie wprowadzonych wartości natężenia ruchu i liczby linii obsługi, dane są przekazywane do funkcji generującej wykres.

2. **Obliczenie wartości współczynnika blokady**: Przed generowaniem wykresu, funkcja oblicza współczynnik blokady, korzystając z wprowadzonych danych wejściowych i odpowiednich formuł matematycznych.

3. **Generowanie wykresu**: Na podstawie obliczonego współczynnika blokady oraz różnych wartości natężenia ruchu, generowany jest wykres. Wykres może być przedstawiony w postaci linii lub punktów, w zależności od preferencji.

4. **Prezentacja wykresu**: Wygenerowany wykres zostaje wyświetlony na drugim ekranie aplikacji, umożliwiając wizualizację zależności między natężeniem ruchu a współczynnikiem blokady. Wykres może być dostosowany pod względem skali osi, etykiet, tytułu i innych parametrów, aby zapewnić czytelność i zrozumiałość prezentowanych danych.

Funkcja generowania wykresu jest integralną częścią kalkulatora Erlanga i stanowi pomocne narzędzie do analizy i wizualizacji wyników obliczeń. Umożliwia użytkownikom łatwe zrozumienie zależności między różnymi parametrami systemu telekomunikacyjnego i ich wpływu na współczynnik blokady.
