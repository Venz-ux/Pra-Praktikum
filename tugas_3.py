# bangunan balok
panjang = 12
lebar = 5
tinggi = 8

# menghitung luas, volume dan keliling dari bangunan tersebut
luas = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
volume = panjang * lebar * tinggi
keliling = 2 * (panjang + lebar)

print("Luas bangunan =", luas)
print("Volume bangunan =", volume)
print("Keliling bangunan =", keliling)

# b. apakah luas > 50?
hasil_b = luas > 50
print("Apakah luas lebih dari 50? =", hasil_b)

# c. apakah volume == 480?
hasil_c = volume == 480
print("Apakah volume 480? =", hasil_c)
