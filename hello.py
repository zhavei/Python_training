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