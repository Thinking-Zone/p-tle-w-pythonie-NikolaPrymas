# Program, który znajdzie pierwszą liczbę podzielną przez 7 w zakresie od 1 do 100
for i in range(1, 101):
    if i % 7 == 0:
        print(f"Pierwsza liczba podzielna przez 7 to: {i}")
        break  # Zakończenie pętli po znalezieniu liczby podzielnej przez 7
