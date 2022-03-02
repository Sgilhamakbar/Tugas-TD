#variabel
panggilan=  ("Ilham akbar hekmatiar ")
nim=  ("20504244021 ")
kelas=  ("C2.1 ")
matakuliah=  ("Transformasi Digital ")
dosenpembimbing=  ("ayu sandra dewi ")
job=  ("Jobshet 02. Alur Kontrol ")

#menampilkan input user
print    ("Nama             : ", panggilan)
print    ("NIM              : ", nim)
print    ("Kelas            : ", kelas)
print    ("Mata kuliah      : ", matakuliah)
print    ("Dosen pembimbing : ", dosenpembimbing)
print    ("Tugas            : ", job)

print ("_"*60)
print ("           Laporan Praktikum Transformasi Digital           ")
print ("_"*60)

print()

print ("Praktikum membuat program kategori dengan memasukan nilai variasi dari 0,00 sampai 4,00")

nilai = float(input("• masukkan nilai : "))

#variabel nilai dan status
if nilai == 4.00:
    penilaian = "A"
    grade = "sangat baik"
elif nilai >= 3.68:
    penilaian = "A"
    grade = "sangat baik"
elif nilai >= 3.34:
    penilaian = "A-"
    grade = "hampir sangat baik"
elif nilai >= 3.01:
    penilaian = "B+"
    grade = "lebih baik"
elif nilai >= 2.68:
    penilaian = "B"
    grade = "baik"
elif nilai >= 2.34:
    penilaian = "B-"
    grade = "hampir baik"
elif nilai >= 2.01:
    penilaian = "C+"
    grade = "lebih dari cukup"
elif nilai >= 1.01:
    penilaian = "C"
    grade = "cukup"
elif nilai >= 0.01:
    penilaian = "D"
    grade = "kurang"
else :
    penilaian = "E"
    grade = "jelek"

print ("nilai anda adalah = ", penilaian)
print ("status            = ", grade)
