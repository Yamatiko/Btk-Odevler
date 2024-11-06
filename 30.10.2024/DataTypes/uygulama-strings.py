title = "Python ile Programlama Dersleri"

# 1- 'title' değişkeni içerisindeki karakter sayısı nedir?
karakterSayisi = len(title)
print(karakterSayisi)
# 2- 'title' içerisindeki 'Python' kelimesini alın.
print(title[0:6])

# 3- 'title' değişkeninin ilk 5 ve son 5 karakterini alın.
print(title[0:6], title[-6:-1])

# 4- 'title' değişkenini tersten yazdırınız.
print(title[::-1])

# 5- Klavyeden girilen öğrenci bilgisine göre örnek verilen cümleyi yazdırınız.
#    Örnek: Çınar Turan isimli öğrencinin 1.notu 60, 2.notu 60 ve not ortalaması 60 olarak hesaplanmıştır.

ogrenciAd = input("Adınızı girin: ")
ogrenciSoyad = input("Soyadınızı girin: ")
birinciNot = int(input("1. sınav notunuzu girin: "))
ikinciNot = int(input("2. sınav notunuzu girin: "))
notOrtalamasi = (birinciNot + ikinciNot)/2

#print("Örnek:", ogrenciAd, ogrenciSoyad, "isimli öğrencinin 1.notu", str(birinciNot), ", 2.notu ", str(ikinciNot), "ve not ortalaması", str(notOrtalamasi), "olarak hesaplanmıştır.")

#Yukarıda baya amelelik yapmışım

sonuc = f"{ogrenciAd} {ogrenciSoyad} isimli öğrencinin 1.notu {birinciNot}, 2.notu {ikinciNot} ve not ortalaması {notOrtalamasi} olarak hesaplanmıştır."
print(sonuc)