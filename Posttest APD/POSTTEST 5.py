daftarUser = [['admin', '0000']]
dataPajak = {}
adminLogin = False
pajakPenghasilan = 0
pajakBumiDanBangunan = 0


def register():
    global daftarUser
    namaUser = str(input('\nMasukkan nama user anda: '))
    passwordUser = str(input('Masukkan password anda: '))

    if [namaUser, passwordUser] in daftarUser:
        print('Nama user sudah ada')
        return
    else:
        tokenUser = [f'{namaUser}', f'{passwordUser}']

        daftarUser.append(tokenUser)
        print(f'''\n
                =======================================
                Selamat, anda berhasil register dengan:
                    Nama User   : {namaUser}
                    Password    : {passwordUser}
                =======================================
                ''')
        return

def login():
    global daftarUser 
    print('\nSilahkan login')
    namaUser = str(input('Masukkan nama user anda: '))
    passwordUser = str(input('Masukkan password anda: '))

    if [namaUser, passwordUser] == ['admin', '0000']:
        admin()
    elif [namaUser, passwordUser] in daftarUser:
        program()
    else:
        print('\nNama user atau password salah!')
        login()


def admin():
    global daftarUser
    global dataPajak
    print('''
            1. Lihat List User dan Password
            2. Lihat Data WP
            3. Hapus Akun
            4. Logout
''')
    while True:
        option = str(input('Masukkan pilihan anda:'))

        if option == '1':
            print(daftarUser)
        elif option == '2':
            print(dataPajak)
        elif option == '3':
            hapusAkun()
        elif option == '4':
            break
        else:
            'Opsi tidak ada'


def hapusAkun():
    print(daftarUser)
    while True:
        opsi = abs(int(input('Pilih akun yang ingin di hapus (ID akun sesuai urutan ditunjukkan): ')))
        if opsi <= len(daftarUser) and opsi != 0 and opsi != 1:
            del daftarUser[opsi-1]
            break
        else:
            print('ID akun tidak ada!')


def program():
    global dataPajak
    global pajakPenghasilan
    global pajakBumiDanBangunan

    print('\nMenjalankan program...')
    nama = str(input('Masukkan nama anda: '))
    alamat = str(input('Masukkan alamat rumah anda: '))
    nohp = str(input('Masukkan No. HP anda: '))

    dataPajak.update({f'Data {nama}' : {'Nama WP' : nama,
                                        'Alamat WP' : alamat,
                                        'No. HP WP' : nohp
                      }})


    while True:
        pilihan = listPajak()

        if pilihan == '1':
            pajakPenghasilan = pph()
            print('Data telah di masukkan')
        elif pilihan == '2':
            pajakBumiDanBangunan = pbb()
            print('Data telah di masukkan')
        elif pilihan == '3':
            dataPajak.update({f'Data Perpajakan {nama}' : {'Pajak Penghasilan' : pajakPenghasilan,
                                                           'Pajak Bumi dan Bangunan' : pajakBumiDanBangunan
                                                           }})
            break


def listPajak():
    print('''
        1. Pajak Penghasilan
        2. Pajak Bumi dan Bangunan
        3. Logout
''')
    pilihan = str(input('\nMasukkan pilihan yang diinginkan: '))

    if pilihan == '1':
        return pilihan
    elif pilihan == '2':
        return pilihan
    elif pilihan == '3':
        return pilihan
    else:
        'Pilihan tidak tersedia'


def opsi():
    option = str(input('Masukkan pilihan anda: '))

    if option == '1':
        return option
    elif option == '2':
        return option
    elif option == '3':
        return option
    else:
        print('Pilihan tidak tersedia')


def pph():
    pajakPenghasilan = abs(float(input('Silahkan masukkan penghasilan anda tiap bulan: ')))
    pajakPenghasilan = pajakPenghasilan * 12

    if pajakPenghasilan <= 60000000:
        pajakPenghasilan = pajakPenghasilan * 5 / 100
        return pajakPenghasilan
    elif pajakPenghasilan <= 250000000:
        pajakPenghasilan = pajakPenghasilan * 15 / 100
        return pajakPenghasilan
    elif pajakPenghasilan <= 500000000:
        pajakPenghasilan = pajakPenghasilan * 25 / 100
        return pajakPenghasilan
    elif pajakPenghasilan <= 5000000000:
        pajakPenghasilan = pajakPenghasilan * 30 / 100
        return pajakPenghasilan
    elif pajakPenghasilan > 5000000000:
        pajakPenghasilan = pajakPenghasilan * 35 / 100
        return pajakPenghasilan


def pbb():
    bumi = int(input('Masukkan meter persegi bumi yang dimiliki: '))
    bangunan = int(input('Masukkan meter persegi bumi yang dipakai untuk bangunan: '))

    bumi = abs(bumi) * 5000000
    bangunan = abs(bangunan) * 1000000

    njop = bumi + bangunan
    if njop < 1000000000:
        njoppersen = 20 / 100
    else:
        njoppersen = 40 / 100
    
    njkp = njoppersen * (njop - 12000000)

    pajakBumiDanBangunan = 0.5 / 100 * njkp
    return pajakBumiDanBangunan


while True:
    print('''
            1. Register
            2. Login
            3. Exit
''')
    option = opsi()

    if option == '1':
        print(daftarUser)
        register()
    elif option == '2':
        login()
    elif option == '3':
        print('Program Selesai!')
        exit()
    else:
        print('Pilihan tidak tersedia!')