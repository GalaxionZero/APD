nama = str(input("Masukkan Nama anda: "))
nim = int(input("Masukkan NIM anda: "))
kelas = str(input("Masukkan Kelas anda: "))
umur = int(input("Masukkan Umur anda: "))
tinggibadan = float(input("Masukkan Tinggi Badan anda: "))
beratbadan = float(input("Masukkan Berat Badan anda: "))
intnim = str(nim)
terakhirnim = intnim[-3:]
nim3terakhir = int(terakhirnim)

print(f"Nama saya {nama} dengan NIM {nim} dari kelas {kelas}. Saya berumur {umur} dengan tinggi badan {tinggibadan} dan berat badan {beratbadan}")
print(f"Tiga angka terakhir NIM anda adalah {nim3terakhir}")
print(f"Tiga angka terakhir NIM setelah dimoduluskan 4 adalah {nim3terakhir % 4}")