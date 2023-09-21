nama = str(input("Masukkan Nama anda: "))
nim = int(input("Masukkan NIM anda: "))
kelas = str(input("Masukkan Kelas anda: "))
umur = int(input("Masukkan Umur anda: "))
tinggibadan = float(input("Masukkan Tinggi Badan anda (cm): "))
beratbadan = float(input("Masukkan Berat Badan anda (kg): "))
strnim = str(nim)
intnim = strnim[-3:]
nim3terakhir = int(intnim)

print(f"Nama saya {nama} dengan NIM {nim} dari kelas {kelas}. Saya berumur {umur} tahun dengan tinggi badan {tinggibadan}cm dan berat badan {beratbadan}kg")
print(f"Tiga angka terakhir NIM anda adalah {nim3terakhir}")
print(f"Tiga angka terakhir NIM setelah dimoduluskan 4 adalah {nim3terakhir % 4}")