wynik = []
def sprawdz(string):
    bufor = []
    bufor = list(string)
    if (bufor[0] == bufor[-1]):
        wynik.append(string)
    else:
        return False


with open("przyklad.txt","r") as file:
    x = file.read()
    x = x.splitlines()
    for i in range(len(x)):
        sprawdz(x[i])
print(f"{len(wynik)} {wynik[0]}")