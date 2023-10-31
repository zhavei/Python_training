def mencari_luas_persegi_panjang (panjang, lebar):
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang

class Name:
    namaa = "dicoding uhuy"

namaku = Name()
print(namaku.namaa)

namaku2 = namaku.namaa = "bebek betelor"
print(namaku2)
#construktor
class Mobil:
    # Atribut Instance
    def __init__(self):
        self.warna = 'Merah'
        self.model = "sport"
        
mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.model)

# Mengubah atribut instance
mobil_1.warna = "Hitam"

# Menampilkan kembali atribut warna
print(mobil_1.warna)
print(mobil_2.warna)

class Mobilan:
    def __init__(self, warna, merek, kecepatan) -> None:
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

mobil_3 = Mobilan("hitam", "duck car", 300)
mobil_4 = Mobilan(warna="grey jasa" ,merek="bugati",kecepatan=750)

print(mobil_3.warna)
print(mobil_3.merek)
print(mobil_3.kecepatan)
print(mobil_4.kecepatan)

def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")
    return wrapper

# Dekorasi fungsi dengan decorator
@my_decorator
def say_hello():
    print("Hello, world!")

# Memanggil fungsi yang sudah didekorasi
say_hello()

class MobilTrek:
    def __init__(self, warna, merek, kecepatan) -> None:
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_speed(self):
        self.kecepatan += 10

mobil_5 = MobilTrek("Merah", "DicodingCar", 160)
print("sebelom di tambaik speed")
print(mobil_5.kecepatan)

mobil_5.tambah_speed()
print("Setelah ditambahkan: ")
print(mobil_5.kecepatan)

#static method
class Mobils:
    def __init__(self, merek):
        self.merek = merek
    
    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobils")
        
Mobils.intro_mobil()
mobil_6 = Mobils("DicodingCar")
mobil_6.intro_mobil()

#class method

class Mobill:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobill(cls):
        print("Ini adalah metode dari kelas Mobill")

    @classmethod
    def intro_mobilli(*args):
        print(args)
        
Mobill.intro_mobill()
mobil_1 = Mobill("DicodingCar")
mobil_1.intro_mobill()

Mobill.intro_mobilli()
mobil_1 = Mobill("DicodingCar")
mobil_1.intro_mobilli()

#inheritance pewarisan
class MobilSeport:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10


class MobilMahal(MobilSeport):
    def turbo(self):
        self.kecepatan += 50

    def tambah_kecepatan(self):     # tambah_kecepatan
        self.kecepatan += 20

# Kelas Mobil Dasar
mobil_6 = MobilSeport("Merah", "DicodingCar", 160)
print(mobil_6.kecepatan)

# Kelas Mobil Sport
mobil_sport_1 = MobilMahal("Hitam", "DicodingSportCar", 160)
print(mobil_sport_1.kecepatan)
mobil_sport_1.turbo()
print(mobil_sport_1.kecepatan)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)

class MobilBaru:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10

class MobilSportBaru(MobilBaru):
    def turbo(self):
        self.kecepatan += 50

    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("Kecepatan Anda meningkat! Hati-Hati!")

# Kelas Mobil Sport
mobil_sport_1 = MobilSportBaru("Hitam", "DicodingSportCar", 160)
mobil_sport_1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobil_sport_1.kecepatan)

## koding kuis oop python

class Animal:
    def __init__(self, name, age, species) -> None:
        self.name = name
        self.age = age
        self.species = species

class Cat(Animal):
    """Class representing a person"""
    def deskripsi(self):
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
    
    def suara(self):
        return "meoew!"

myCat = Cat("Dico", 3, "Indo")

print(myCat.deskripsi())
print(myCat.suara())

#format code

class Kalkulator:
    """kalkulator tambah kurang"""
    def __init__(self, _i):
        self.i = _i
    def tambah(self, _i): return self.i + _i
    def kurang(self, _i):
        return self.i - _i
    
## regex

import re

pola= '^a...s$'
string_tes= 'abyss'
hasil= re.match(pola, string_tes)
 
if hasil:
    print("Pencarian berhasil.")
else:
    print("Pencarian gagal.")

## math
import math
print(math.sqrt(25)) 
print(math.pi) 

##file: hello.py

import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', action='store_true', help="tampilkan output")
args = parser.parse_args()
 
if args.output:
   print("Halo, ini merupakan sebuah output dari panggildicoding.py")

## panda library

import pandas as pd

data = {
    "nama": ["john", "jane", "jin", "bebek"],
    "usia": [25, 63, 56, 32],
    "pekerjaan": ["kang teyoy", "kang krupuk", "kang bangunan", "kang ayam"]
}

df = pd.DataFrame(data)

print(df)

## matplotlib

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.title("Contoh Plot Garis")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")

plt.show()

##seaborn

import seaborn as sns
# Contoh data
tips = sns.load_dataset('tips')  # Memuat dataset tips dari Seaborn
 
# Contoh plot histogram
sns.histplot(tips['total_bill'], kde=True)
plt.title('Histogram Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()

##json
import json
 
# contoh JSON:
x = '{ "nama":"Buchori", "umur":22, "Kota":"New York"}'
 
# parse  x:
y = json.loads(x)
 
print(y["umur"])

#pickle

import pickle
contoh_dictionary = {1:"6", 2:"2", 3:"f"}
pickle_keluar = open("dict.pickle","wb")
pickle.dump(contoh_dictionary, pickle_keluar)
pickle_keluar.close()

pickle_masuk = open("dict.pickle", "rb")
contohDictionary = pickle.load(pickle_masuk)
pickle_masuk.close()
 
print(contohDictionary)

##BeautifulSoup web scarping
from urllib.request import urlopen
from bs4 import BeautifulSoup
 
# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")
 
# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
 
# Mencetak judul halaman
print(soup.title)