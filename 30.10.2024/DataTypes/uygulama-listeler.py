# 1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.
markalar = ["Toyota", "Bmw", "Renault", "Mercedes"]

# 2- Liste kaç elemanlıdır?
print(len(markalar))

# 3- Listenin ilk ve son elemanı nedir?
print(markalar[0]) 
print(markalar[-1])

# 4- "Renault" markasını "Togg" ile güncelleyiniz.
markalar[2] = "Togg"
print(markalar)

# 5- "Togg" listenin bir elemanı mıdır?
print("Togg" in markalar)

# 6- Listenin ilk 2 elemanını alınız.
print(markalar[:2])

# 7- Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.
#markalar.append("Ford")
#markalar.append("Citroen")
markalar = markalar + ["Ford", "Citroen"]
print(markalar)
# 8- Listenin son elemanını siliniz.
del markalar[-1]
print(markalar)
# 9- Aşağıdaki verileri liste içerisinde saklayınız.

    # öğrenci1: Yiğit Bilgi 2010 [70,80,90]
    # öğrenci2: Ada Bilgi   2011 [70,70,80]
    # öğrenci3: Çınar Turan 2017 [60,60,90]

ogrenci1 = ["Yiğit", "Bilgi", 2010, [70,80,90]]
ogrenci2 = ["Ada", "Bilgi", 2011, [70,70,80]]
ogrenci3 = ["Çınar", "Turan", 2017, [60,60,90]]

ogrenciler = [ogrenci1, ogrenci2, ogrenci3]

# 10- Öğrencilerin yaşlarını hesaplayınız.
yasYigit = 2024 - ogrenci1[2]
yasAda = 2024 - ogrenci2[2]
yasCinar = 2024 - ogrenci3[2]



# 11- Öğrencilerin not ortalamalarını hesaplayınız.
ortYigit = (ogrenci1[3][0]+ogrenci1[3][1]+ogrenci1[3][2])/3
ortAda = (ogrenci2[3][0]+ogrenci2[3][1]+ogrenci2[3][2])/3
ortCinar = (ogrenci3[3][0]+ogrenci3[3][1]+ogrenci3[3][2])/3

print(ortYigit)
print(ortAda)
print(ortCinar)