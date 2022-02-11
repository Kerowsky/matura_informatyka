bufor1 = []
bufor2 = []
suma = 0
with open("dane1.txt", "r") as plik1:
    cyfry = plik1.readlines()
    for x in cyfry:
        bufor1.append(x.split())
with open("dane2.txt", "r") as plik2:
    cyfry = plik2.readlines()
    for x in cyfry:
        bufor2.append(x.split())
for i in range(len(bufor1)):
    if(bufor1[i][9] == bufor2[i][9]):
        suma = suma + 1
print(suma)


