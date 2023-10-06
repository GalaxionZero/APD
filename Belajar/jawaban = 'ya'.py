jawaban = 'ya'
hitung = 0

while jawaban == 'ya':
    hitung += 1
    jawaban = str(input('Mau mengulang program? '))

print(f'Jumlah perulangan = {hitung}')