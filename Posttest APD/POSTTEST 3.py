nama = str(input('Masukkan nama anda: '))
berat = float(input('Masukkan berat badan anda (mg): '))
tinggi = float(input('Masukkan tinggi badan anda (km): '))
print(f'Nama: {nama}')

beratkg = berat * 10e-6
tinggim = tinggi * 10e2
print (f'Berat Badan: {beratkg}kg')
print(f'Tinggi Badan: {tinggim}m')

bmi = beratkg / (tinggim ** 2)
print(f'BMI: {bmi}')

if bmi < 18.5:
    print('Anda underweight')
elif bmi < 24.9:
    print('Anda normal')
elif bmi < 29.9:
    print('Anda overweight')
else:
    print('Anda obesitas')

