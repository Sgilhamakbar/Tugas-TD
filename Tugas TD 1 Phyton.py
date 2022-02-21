#variabel
panggilan=  ("Ilham akbar hekmatiar ")
nim=  ("20504244021 ")
kelas=  ("C2.1 ")
matakuliah=  ("Transformasi Digital ")
dosenpembimbing=  ("ayu sandra dewi ")
job=  ("Jobshet 1 bahasa pemograman phyton ")

#menampilkan input user
print    ("Nama: ", panggilan)
print    ("NIM: ", nim)
print    ("Kelas: ", kelas)
print    ("Mata kuliah: ", matakuliah)
print    ("Dosen pembimbing: ", dosenpembimbing)
print    ("Tugas: ", job)

print ("_"*60)
print ("          Laporan Praktikum Transformasi Digital")
print ("_"*60)

#operasi menghitung luas dan volume balok

print    ("Membuat program untuk menghitung luas permukaan dan volume dari balok, berikut programnya:")

p = int(input("Nilai Panjang  = "))
l = int(input("Nilai Lebar    = "))
t = int(input("Nilai Tinggi   = "))

print()

L = (2*p*l) + (2*p*t) + (2*l*t)
V = p*l*t

print    ("L = (2*p*l) + (2*p*t) + (2*l*t)")
print    ("V = p*l*t")

print ()

print    ("Luas Permukaan Balok Adalah  = ", L)
print    ("Volume Balok Adalah          = ", V)

print ("_"*60)

#soal latihan01.py

print    ("soal!!")
print    ("1. Sebuah balok berukuran panjang 16 cm lebar 10 cm dan tinggi 8 cm, maka luas permukaan balok adalah ")
print    ("a. 488 cm²")
print    ("b. 654 cm²")
print    ("c. 288 cm²")
print    ("d. 736 cm²")

print    ()

p = 16
l = 10
t = 8

print    ("Dikerahui: ")
print    ("Panjang balok        = ", p)
print    ("lebar balok          = ", l)
print    ("tinggi balok         = ", t)

print ()

print    ("jawab: ")
print    ("•Mencari Luas Permukaan Balok")
print    ("L = (2*p*l) + (2*p*t) + (2*l*t)")
print    ("L = (2*16*10) + (2*16*8) + (2*10*8)")
print    ("L = (320) + (256) + (160)")
print    ("L = 736")

print()

print    ("• Mencari Volume Balok")
print    ("V = p*l*t")
print    ("V = 16*10*8")
print    ("V = 1280")

print ()

print    ("Luas Permukaan Balok = ", (2*p*l) + (2*p*t) + (2*l*t), "cm²")

print    ("Volume Balok         =", p*l*t, "cm³")

