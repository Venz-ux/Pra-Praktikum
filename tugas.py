data_string = "Muhammad Veno Rizqi Ramadhan"
print("Nama : ", data_string)
data_integer = 20 
print("Umur : ", data_integer, "tahun")
data_float = 48 
print("Berat : ",  data_float, "kg")



angka_string = "123"
angka_float = 45.67
angka_integer = 89

# 1. konversi angka_string menjadi integer
int(angka_string)
print("data = ", angka_string, "type = ", type(angka_string))

# 2. konversi angka_float menjadi integer
int(angka_float)
print("data = ", angka_float, "type = ", type(angka_float))

# 3. konversi angka_integer menjadi float
angka_integer_float = float(angka_integer)
print("data = ", angka_integer_float, "type = ", type(angka_integer_float))

# 4. konversi angka_integer menjadi string
angka_integer_str = str(angka_integer)
print("data = ", angka_integer_str, "type = ", type(angka_integer_str))


# a. meminta input usia (integer)
usia = int(input("masukan usia: "))
print("usia ", usia, ", type = ", type(usia))

# b. meminta input tinggi badan (float)
tinggi_badan = float(input("masukan tinggi badan: "))
print("tinggi badan ", tinggi_badan, ", type = ", type(tinggi_badan))

# c. meminta input nama (string)
nama = input("masukan nama: ")
print("nama ", nama, ", type = ", type(nama))
