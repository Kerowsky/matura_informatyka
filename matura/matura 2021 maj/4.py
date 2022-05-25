polecenia = []
temp = ""
with open("instrukcje.txt", "r") as file:
    for lines in file:
        polecenia.append(lines.strip())

for i in range(len(polecenia)):
    if polecenia[i].split()[0] == "DOPISZ":
        temp = temp + str(polecenia[i].split()[1])
    if polecenia[i].split()[0] == "ZMIEN":
        temp = temp[:-1]
        temp = temp + str(polecenia[i].split()[1])
    if polecenia[i].split()[0] == "USUN":
        temp = temp[:-1]
    if polecenia[i].split()[0] == "PRZESUN":
        for y in temp:
            if y == polecenia[i].split()[1]:
                if y == "Z":
                    tempnumber = ord("A")
                    indeks = temp.index(y)
                    temp = temp[:indeks] + chr(tempnumber) + temp[indeks + 1:]
                    break
                else:
                    tempnumber = ord(polecenia[i].split()[1])
                    tempnumber = tempnumber + 1
                    indeks = temp.index(y)
                    temp = temp[:indeks] + chr(tempnumber) + temp[indeks + 1:]
                    break
print(temp)