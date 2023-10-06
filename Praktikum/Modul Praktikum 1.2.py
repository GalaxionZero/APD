#Memasukkan angka 
input = int(input('Masukkan angka: '))

#Mengubah angka menjad variabel yang bisa dibaca
angka = int(input)

#Mencari apakah angka yang dimasukkan dapat dibagi dua tanpa adanya desimal
if angka % 2 == 0:
    print(angka, 'is an even number')
else:
    print(angka, 'is an odd number')