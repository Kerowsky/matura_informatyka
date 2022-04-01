bufor = []
stats = {}

with open("galerie.txt", "r") as file: # Odczyt pliku
    for i in file:
        bufor.append(i.split()) #Każdą linijke dodaj do bufora

for v in range(len(bufor)): #Dla każdej linijki w zakresie len(bufor) jeśli nie ma jej w dict stat dodaj do dict jeśli jest dodaj 1
    if not bufor[v][0] in stats:
        stats[bufor[v][0]] = 1
    else:
        stats[bufor[v][0]] += 1
file.close()

with open("wynik4_1.txt", "w") as zapis:
    for k, v in stats.items():
        zapis.write(f"{k}: {v} \n") #Wypisz tak ja proszone w zadaniu
zapis.close()