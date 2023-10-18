import os
ulang = 0
listuser = []
retry = 1
bmi = 0.00


def eexit():
    print('=' * 25)
    print('     Program Selesai')
    print('=' * 25)
    exit()


def opsi():
    global ulang
    pilihan = ''

    while pilihan != 3:
        pilihan = str(input('Masukkan pilihan anda: '))
        if pilihan == '1':
            return pilihan
        elif pilihan == '2':
            return pilihan
        elif pilihan == '3':
            return pilihan
        else:
            print('Pilihan tidak tersedia')


def register():
    try:
        nama = str(input('\nMasukkan nama anda: '))
        nim = str(input('Masukkan 3 angka dibelakang NIM anda sebagai password (Jika ada 0 di depan seperti 023, akan diubah menjadi 23): '))
        nim = nim.lstrip('0')

        logintoken = {'namauser': nama, 'nimuser': nim}

        listuser.append(logintoken)
        print(f'''\n
              =======================================
              Selamat, anda berhasil register dengan:
                    Nama User   : {nama}
                    Password    : {nim}
              =======================================
                
                   Redirecting to Login page...
                ''')
    except:
        print('Hello')


def login():
    global ulang
    while True:
        try:
            nama = str(input('Masukkan nama user anda: '))
            nim = str(input('Masukkan password anda: '))

            logintoken = {'namauser': nama, 'nimuser': nim}

            if logintoken not in listuser:
                raise Exception('\nAnda belum register atau nama user dan password salah')
            return ending()
        
        except Exception as f:
            ulang += 1
            print(f)
            if ulang == 3:
                eexit()


def checkvalue(value):
    if value < 18.5:
        return 'underweight'
    elif value < 24.9:
        return 'normal'
    elif value < 29.9:
        return 'overweight'
    else:
        return 'obesitas' 


def ending():
    global retry
    global ulang
    while True:
        try:
            x = getbmi()
            print(f'''\nAnda dinyatakan {checkvalue(x)}
                        BMI anda {x}
                  ''')
            retry = int(input('''\nIngin mengulang program?
                              1. Yes
                              2. No
                              '''))
            if retry == 1:
                os.system('cls')
                break
            else:
                eexit()
        except KeyboardInterrupt:
            eexit()


def getbmi():
    global bmi
    print('\nInitiating Program Kalkulator BMI')
    while True:
        berat = float(input('Masukkan berat badan anda (mg): '))
        tinggi = float(input('Masukkan tinggi badan anda (km): '))
        beratkg = abs(berat) * 10e-6
        tinggim = abs(tinggi) * 10e2

        bmi = beratkg / (tinggim ** 2)
        return bmi


while ulang < 3:
    print('''
==========================
1. Register
2. Login and Enter Program
3. Exit Program
==========================
''')
    pilihan = opsi()

    if pilihan == '1':
        register()
    elif pilihan == '2':
        login()
    elif pilihan == '3':
        eexit()
else:
    eexit()