# Aşağıdaki öğrenci bilgilerini dictionary listesinde saklayınız.
    # 101 Yiğit Bilgi 2010 (40,80,90)
    # 102 Ada Bilgi   2012 (80,80,80)
    # 103 Çınar Turan 2017 (70,70,70)

ogrenciler = {
    101 : ["Yiğit Bilgi", 2024-2010, (40,80,90)],
    102 : ["Ada Bilgi", 2024-2012, (80,80,80)],
    103 : ["Çınar Turan", 2024-2017, (70,70,70)] 
}



# Klavyeden girilen öğrenci numarasına göre aşağıdaki cümleyi yazdırınız.
    # 101 numaralı Yiğit Bilgi ismindeki öğrencinin yaşı 14 ve not ortalaması 70.

ogrenciNo = int(input("Numaranızı girin: "))


mesaj = f"{ogrenciNo} numaralı {ogrenciler[ogrenciNo][0]} ismindeki öğrencinin yaşı {ogrenciler[ogrenciNo][1]} ve not ortalaması {sum(ogrenciler[ogrenciNo][2])/len(ogrenciler[ogrenciNo][2])}"
print(mesaj)