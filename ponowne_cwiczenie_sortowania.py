lista = [1, 5, 2, 7, 30, 100, 4, 13, 10]

print(f"Lista przed sortowanie {lista}")
dlugosc = len(lista)

for j in range(dlugosc):
    for i in range(dlugosc - j -1):
        if lista[i+1] < lista[i]:
            lista[i+1], lista[i] = lista[i], lista[i+1]
print(f"Lista po sortowaniu {lista}")