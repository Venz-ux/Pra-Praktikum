usia = int(input("Masukan usia anda: "))

if usia >= 0 and usia <= 12:
    print("kategori usia anda: Anak_anak")
elif usia >= 13 and usia <= 17:
    print("kategori usia anda: Remaja")
elif usia >= 18 and usia <= 59:
    print("kategori usia anda: Dewasa")
elif usia >= 60:
    print("kategori usia anda: Lansia")
else:
    print("usia tidak valid")
print("akhir dari program")