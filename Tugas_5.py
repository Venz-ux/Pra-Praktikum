# Bilangan ganjil dan genap dari 1 sampai 50
ganjil = []
genap = []
for i in range(1, 51):
    if i % 2 == 0:
        genap.append(i)
    else:
        ganjil.append(i)

print("Bilangan ganjil:")
print(ganjil)
print("Bilangan genap:")
print(genap)


# Bilangan prima antara 1 sampai 100
print("Bilangan prima 1 sampai 100:")
for angka in range(2, 101):
    prima = True
    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            prima = False
            break
    if prima:
        print(angka, end=" ")
print()