# name = input("kecrotkan nama anda : ")
# print("nama dia adalah " + name)
# ini komen huhuy

# print(id(name))

# x = 'Dicoding'
# x[0] = 'F'

# name = "Perseus Evans"
# print("Nama saya %s" % (name))

# names = "bebek betelor emas"
# print("nama saya {}".format(names))

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# union = set1.union(set2)
# print("union: ", union)

# intesex = set1.intersection(set2)
# print("intersection ", intesex)

# print('''Halo,
# aku ikan,
# aku suka sekali menyelam
# aku tinggal di perairan.
# Badanku licin dan renangku cepat.
# Senang berkenalan denganmu.'''.split('\n'))

# belajar = "ayo gas kan belajar coding di kandang"
# print(belajar.replace("gas kan", "mulai"))

# print("1254".isdecimal())

"""
TODO:
Diberikan sebuah variabel berisi nilai list dengan nama "var_list". 
Berdasarkan list tersebut, cari hal-hal berikut ini:
- Panjang list tersebut dan simpan dengan nama variabel "panjang".
- Nilai maksimal list tersebut dan simpan dengan nama variabel "maksimal".
- Nilai minimal list tersebut dan simpan dengan nama variabel "minimal".
- Berapa banyak angka 605132 dalam list tersebut dan simpan dalam variabel bernama "banyak"

Tips:
- Anda bisa menggunakan berbagai kode yang ada di materi operasi, 
  tidak diperbolehkan memasukan nilai secara langsung.
"""

# # Jangan ubah kode ini
# var_list = [792564, 465231, 203748, 981037, 857219, 314092, 608345, 123907, 736890, 985026, 
# 179430, 450218, 680934, 543187, 978260, 283045, 617902, 405826, 820913, 731095, 
# 592403, 109237, 874956, 605132, 214978, 674519, 391047, 825160, 509317, 768490, 
# 950283, 307491, 487610, 532198, 605132, 160984, 609873, 245016, 879043, 734126, 
# 351809, 670594, 920873, 605132, 596410, 135890, 804512, 683420, 290753, 931560, 
# 175430, 950672, 378490, 284105, 746098, 503624, 605132, 167432, 974810, 519463, 
# 407835, 740326, 281709, 630921, 953284, 605132, 429731, 183607, 369012, 541380, 
# 605132, 217605, 496803, 827309, 153607, 605132, 720459, 381904, 594031, 810235, 
# 673925, 492157, 835096, 260481, 956024, 540329, 806295, 320158, 751903, 980465, 
# 235780, 857943, 605132, 125094, 620493, 913250
# ]

# # TODO: Buat kode Anda di bawah ini
# panjang = len(var_list)
# maksimal = max(var_list)
# minimal = min(var_list)

# banyak = var_list.count(605132)

# print("panjang", panjang)
# print("maksimal", maksimal)
# print("minimal", minimal)
# print("banyak", banyak)

# name = 'Dicoding Indonesia'
# print(f"Hello, saya belajar coding di {name}")

# x = (5, 'program', 1+3j)
# x[1] = 'Dicoding'
# print(x)

#total belanja dico
dico = 750000
# Buat variabel untuk menyimpan potongan harga
diskon = 0.1
# Hitung total harga belanja
total_harga = dico
# Periksa apakah harga belanja lebih dari 500.000
if dico > 500000:
    # Hitung besaran diskon
    diskon_harga = diskon * dico
    # Kurangi harga belanja dengan besaran diskon
    total_harga_dico = total_harga - diskon_harga

# Cetak total harga belanja
print("total belanja dico setelah diskon RP.",total_harga_dico)
print(diskon * dico)
#####################################################################
# Jangan ubah kode ini
dico = 750000
# Tentukan nilai ambang batas untuk mendapatkan diskon
ambang_diskon = 500000
# Tentukan persentase diskon
persentase_diskon = 10
# Hitung total harga belanja Dico setelah mendapatkan diskon
if dico > ambang_diskon:
    diskon = (dico * persentase_diskon) / 100
    total_harga = dico - diskon
else:
    total_harga = dico

# Cetak total harga belanja Dico
print("Total harga belanja Dico setelah mendapatkan diskon:", total_harga)
################################################################################
# Jangan ubah kode ini
dico = 750000
ding = 450000

# Menentukan nilai ambang diskon
ambang_diskon_1 = 500000
ambang_diskon_2 = 600000
ambang_diskon_3 = 750000

# Menentukan persentase diskon untuk masing-masing ambang diskon
persentase_diskon_1 = 0.10  # 10%
persentase_diskon_2 = 0.15  # 15%

# Menghitung total harga belanja Dico setelah mendapatkan diskon
total_harga = 0  # Inisialisasi total harga

if dico >= ambang_diskon_1 and dico <= ambang_diskon_2:
    total_harga = dico * (1 - persentase_diskon_1)
elif dico > ambang_diskon_2 and dico <= ambang_diskon_3:
    total_harga = dico * (1 - persentase_diskon_2)
else:
    total_harga = dico  # Tidak ada diskon

# Mencetak total harga belanja Dico setelah mendapatkan diskon
print("Total harga belanja Dico setelah diskon:", total_harga)
#########################################################################
# Buat variabel untuk menyimpan potongan harga
diskon_1 = 0.1
diskon_2 = 0.15

# Hitung total harga belanja
total_harga = ding

# Periksa apakah harga belanja lebih dari 500.000
if ding > 500000:
    # Periksa apakah harga belanja lebih dari 650.000
    if ding > 650000:
        # Hitung total harga belanja setelah diskon
        total_harga = total_harga * (1 - diskon_2)
    else:
        # Hitung total harga belanja setelah diskon
        total_harga = total_harga * (1 - diskon_1)

# Cetak total harga belanja
print("total si dico setelah diskon", total_harga)


##menu_sedia = input("daging ayam")
menu_sedia = "daging ayam"

if menu_sedia == "daging ayam":
    print(menu_sedia)
elif menu_sedia == "daging ebek":
    print("adanya gading bebek")
else:
    print("g ada launknya")
    

##string kosong di anggap false oleh python
x = ""

if x:
    print("Ini True")

tinggi_badan = 120

if tinggi_badan >=160:
    print("Anda boleh menaiki roller coaster")
else:
    print("Anda tidak diperbolehkan menaiki roller coaster")


mumtaz = True
print("greate score") if mumtaz else ("not greate")

#TUPLE ternary
kelulusan = True

kelas_1 = ("yeay, anda lulus", "coba lagi taon depan")[kelulusan]
print(kelas_1)

rangee = range(1,11)

for i in rangee:
    print(i)

counter_range = 1

while counter_range <= 11:
    print(counter_range)
    counter_range +=1

for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)

for i in range(2):
    print("perulangan luar: ", i)
    for j in range(10):
        print("perulangan dalam:", j)
        if j == 1:
            break

#else setelah (in) for & loop break
numbersi = [1, 2, 3, 4, 5]

for num in numbersi:
    if num == 6:
        print("angka di temukan oke!")
        break
    else:
        print("angka jg g tau dimn")


## else after while

counto = 0

while counto < 3:
    print("Dicoding Indonesia")
    counto += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False) .", counto)

n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")

x = 10

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")

angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)
#Namun, alih-alih membuat kode program seperti di atas. Anda dapat melakukan hal berikut.
angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

"""
TODO:
Buatlah sebuah variabel bertipe list bernama "evenNumber" dengan ketentuan:
- variabel tersebut menampung bilangan genap dari 0 hingga 500 (ingat 0 dan 500 termasuk).
Tips:
Anda bisa menggunakan loop dan if atau list comprehension untuk memudahkan.
"""
numberRange = range(0,501)
evenNumber = []
for number in numberRange:
    if number % 2 == 0:
        evenNumber.append(number)
        print(evenNumber)


#penanganan kesalahan syntx dan exception
z = 0
try:
    print(1/z)
except ZeroDivisionError:
    print("tidak bisa 1 di bagi 0")

# try except else finally

var_dict = {"rata_rata": "1.0"}

try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")