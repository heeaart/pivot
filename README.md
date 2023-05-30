# Pivot

## 1. Definicja funkcji quicksort:
Funkcja quicksort przyjmuje dwa argumenty: tab, który jest listą do posortowania, i lvl, który jest poziomem rekursji (domyślnie ustawionym na 0).
Funkcja zwraca posortowaną listę.

## 2.Warunek końcowy:
Pierwszy warunek w funkcji if len(tab) in [0,1]: sprawdza, czy lista tab jest pusta lub ma tylko jeden element.
Jeśli tak, to lista jest już posortowana, więc funkcja zwraca tę samą listę.

## 3. Wybór pivota:
Linia pivot = tab[0] wybiera pierwszy element z listy tab jako pivot.

## 4.Podział listy:
Linia left_part = [x for x in tab[1:] if x <= pivot] tworzy nową listę left_part, która zawiera wszystkie elementy z tab, które są mniejsze lub równe pivotowi.
Linia right_part = [x for x in tab[1:] if x > pivot] tworzy nową listę right_part, która zawiera wszystkie elementy z tab, które są większe od pivota.

## 5. Rekurencyjne wywołanie:
Linia return quicksort(left_part, lvl + 1) + [pivot] + quicksort(right_part, lvl + 1) wykonuje rekurencyjne wywołanie funkcji quicksort dla left_part i right_part.
Wyniki sortowania obu części są połączone z pivotem, tworząc posortowaną listę.

## 6. Test i wydruk:
Blok if __name__ == '__main__': sprawdza, czy kod jest uruchamiany jako skrypt (a nie importowany jako moduł).
Tworzone są dwie listy testowe: tab i tab1.
Linia assert quicksort(tab) == tab1 sprawdza, czy posortowana lista quicksort(tab) jest równa oczekiwanej posortowanej liście tab1. Jeśli nie, program zatrzyma się z błędem.
Linia print(f"sortowanie {quicksort(tab)}") wydrukuje posortowaną listę quicksort(tab) wraz z komunikatem "sortowanie".
Podsumowując, ten kod implementuje algorytm QuickSort, który rekurencyjnie dzieli listę na mniejsze części, sortuje je i łączy w celu ostatecznego posortowania całej listy.
