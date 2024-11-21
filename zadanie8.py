pada = False
licznik_nie = 0

# Pętla będzie trwała, dopóki użytkownik nie odpowie "tak"
while not pada:
    odpowiedz = input("Czy pada? (tak/nie/nie wiem) ").strip().lower()
    
    # Obsługa odpowiedzi "tak"
    if odpowiedz == "tak":
        pada = True
        print(f"Zgadłeś! Liczba odpowiedzi 'nie': {licznik_nie}")
    
    # Obsługa odpowiedzi "nie"
    elif odpowiedz == "nie":
        licznik_nie += 1
        print("Nie pada! Spróbuj ponownie.")
    
    # Obsługa odpowiedzi "nie wiem"
    elif odpowiedz == "nie wiem":
        print("To wyjdź na zewnątrz i się dowiedz.")
    
    # Obsługa niepoprawnych odpowiedzi
    else:
        print("Niepoprawna odpowiedź. Proszę odpowiedzieć 'tak', 'nie' lub 'nie wiem'.")
