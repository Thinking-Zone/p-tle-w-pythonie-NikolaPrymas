import random

# Losowanie, czy pada
pada = random.choice([True, False])

# Zmienna kontrolująca pętlę
zgaduj = True

# Pętla, która będzie pytać użytkownika dopóki nie zgadnie
while zgaduj:
    odpowiedz = input("Czy pada? (t/n) ").strip().lower()

    # Sprawdzenie, czy odpowiedź użytkownika jest poprawna
    if odpowiedz == 't' and pada:
        print("Tak, pada! Brawo!")
        zgaduj = False
    elif odpowiedz == 'n' and not pada:
        print("Nie, nie pada! Brawo!")
        zgaduj = False
    elif odpowiedz == 't' and not pada:
        print("Nie, nie pada. Spróbuj jeszcze raz!")
    elif odpowiedz == 'n' and pada:
        print("Tak, pada. Spróbuj jeszcze raz!")
    else:
        print("Niepoprawna odpowiedź, użyj 't' lub 'n'.")
