#praktikum3_perbandingan_logika.py
nilai = 82
kehadiran = 90

syarat_nilai = nilai >= 75
syarat_hadir = kehadiran >= 80
print("Nilai >= 75      :", syarat_nilai)
print("Kehadiran >= 80  :", syarat_hadir)
print("Lulus (and)      :", syarat_nilai and syarat_hadir)
print("Lulus (or)       :", syarat_nilai or syarat_hadir)

nilai = 70
syarat_nilai = nilai >= 75
print("Setelah nilai = 70")
print("Lulus (and)      :", syarat_nilai and syarat_hadir)
print("Lulus (or)       :", syarat_nilai or syarat_hadir)