# hitung = 0
# for i in range(1, 50):
#     if i > 1:
#         for j in range(2, i):
#             if j % 1 == 0:
#                 break
#         else:
#             print(i)
#             hitung += 1
# print(f'Jumlah bilangan prima dari 1 sampai 50 adalah {hitung}')

# jumlah = 0
# print('Jika anda menginput bilangan negatif maka program akan terhenti!')

# while True:
#     angka = int(input('Masukkan angka: '))
#     if angka >= 0:
#         jumlah = jumlah + angka
#     else:
#         break

# print(f'Jumlah angka yang diinputkan adalah = {jumlah}')

# for i in range(2, 51):
#     if i >= 4 and i % 2 == 0:
#         continue
#     elif i >= 9 and i % 3 == 0:
#         continue
#     elif i >= 25 and i % 5 == 0:
#         continue
#     elif i >= 49 and i % 7 == 0:
#         continue
#     else:
#         print(i)

while True:
    print('''
    1. +
    2. -
    3. *
    4. /
    5. Hentikan program
''')
    pilihan = int(input('Masukkan pilihan nomor operator anda: '))
    if pilihan == 1:
        angka1 = int(input('Masukkan angka pertama: '))
        angka2 = int(input('Masukkan angka kedua: '))
        hasil = angka1 + angka2
    elif pilihan == 2:
        angka1 = int(input('Masukkan angka pertama: '))
        angka2 = int(input('Masukkan angka kedua: '))
        hasil = angka1 - angka2
    elif pilihan == 3:
        angka1 = int(input('Masukkan angka pertama: '))
        angka2 = int(input('Masukkan angka kedua: '))
        hasil = angka1 * angka2
    elif pilihan == 4:
        angka1 = int(input('Masukkan angka pertama: '))
        angka2 = int(input('Masukkan angka kedua: '))
        hasil = angka1 / angka2
    elif pilihan == 5:
        break
    else:
        print('Error Input')
    print(hasil)