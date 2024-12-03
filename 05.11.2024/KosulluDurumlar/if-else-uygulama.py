# Bir aracın yakıt tipine göre (benzin,dizel,lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
benzinFiyat = 39.35
dizelFiyat = 41.71
lpgFiyat = 20.28

ortalamaYakitLt = float(input("100 km'de ortalama yakıt tüketiminizi girin: "))
aracTuru = input("Araç türünüzü giriniz: (benzin, dizel, lpg) ")
gidilenMesafe = float(input("Aldığınız yol kaç km? "))

if aracTuru == "benzin" : 
    print("Yakıt masrafınız : ",round(((ortalamaYakitLt * benzinFiyat) / 100) * gidilenMesafe, 2), "tl")
elif aracTuru == "dizel" :
    print("Yakıt masrafınız : ",round(((ortalamaYakitLt * dizelFiyat) / 100) * gidilenMesafe, 2), "tl")
elif aracTuru == "lpg" : 
    print("Yakıt masrafınız : ",round(((ortalamaYakitLt * lpgFiyat) / 100) * gidilenMesafe, 2), "tl")
else :
    print("Yanlış tür girdiniz.")
    
# Bir öğrencinin 2 yazılı bir sözlü notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen değerlendirmeyi yazdırınız.

birinciYazili = int(input("1. yazılı notunuzu giriniz: "))
ikinciYazili = int(input("2. yazılı notunuzu giriniz: "))
birinciSozlu = int(input("1. sözlü notunuzu giriniz: "))

ortalama = (birinciSozlu + birinciYazili + ikinciYazili) / 3

if 0 < ortalama <= 24 :
    print(0)
elif 25 < ortalama <= 44 :
    print(1)
elif 45 < ortalama <= 54 :
    print(2)
elif 55 < ortalama <= 69 :
    print(3)
elif 70 < ortalama <= 84 :
    print(4)
elif 85 < ortalama <= 100 :
    print(5)
else :
    print("Notunuz aralığın dışında???")


#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

