retry = 'y'

def getUserInput():
    while True:
        try:
            x = int(input('Masukkan nilai Anda [0 - 100]: '))
            if 0 <= x <= 100:
                return x
            else:
                print('Nilai harus di dalam range 0 hingga 100!')
        except:
            print('Input harus berupa angka bilangan bulat!')

def checkValue(value):
    if value >= 90:
        return 'A+'
    elif value >= 80:
        return 'A-'
    elif value >= 75:
        return 'B+'
    elif value >= 70:
        return 'B-'
    elif value >= 65:
        return 'C+'
    elif value >= 60:
        return 'C-'
    elif value >= 50:
        return 'D'
    else:
        return 'E'

while retry != 'n':
    try:
        x = getUserInput()
        print(checkValue(x))
        retry = input('Ingin mengulangi program? (y/n): ')
        os.system('cls')
    except KeyboardInterrupt:
        print('Anda telah membatalkan input.')
    
print('\nProgram Selesai!')