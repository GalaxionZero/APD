import random

namaAtlit1 = [
'Karch Kiraly',
'Gilberto Amauri de Godoy Filho',
'Misty May-Treanor',
'Kerri Walsh Jennings',
'Emanuel Rego',
'Logan Tom',
'Zhu Ting',
'Sergey Tetyukhin',
'Sheilla Castro',
'Matt Anderson'
]


print('Sort menurut alphabet dari A-Z')
sorted1 = enumerate(sorted(namaAtlit1), start=1)
for nomor1, namaAtlit in sorted1:
    print(f"{nomor1}. {namaAtlit}")

print('\nSort menurut alphabet dari Z-A')
sorted1 = enumerate(sorted(namaAtlit1, reverse=True), start=1)
for nomor1, namaAtlit in sorted1:
    print(f"{nomor1}. {namaAtlit}")

print('\nSort menggunakan pendek nama')
sort_panjang = enumerate(sorted(namaAtlit1, key=len), start=1)
for namaAtlit in sort_panjang:
    print(namaAtlit)

print('\nSort menggunakan panjang nama')
sort_panjang_reverse = enumerate(sorted(namaAtlit1, key=len, reverse=True), start=1)
for namaAtlit in sort_panjang_reverse:
    print(namaAtlit)

print('\nSort menggunakan random number sehingga terurut secara acak')
angka_acak = random.sample(range(1, 100), len(namaAtlit1))
nama_dan_angka = list(zip(namaAtlit1, angka_acak))
nama_dan_angka.sort(key=lambda x: x[1])
for nomor, (namaAtlit, angka) in enumerate(nama_dan_angka, start=1):
    print(f"{nomor}. {namaAtlit} - Angka: {angka}")