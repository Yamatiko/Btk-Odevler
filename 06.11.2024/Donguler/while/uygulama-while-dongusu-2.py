#    Klavyeden girilen n sayıdaki öğrenci bilgisini liste içerisinde saklayınız.
#    ** dictionary listesi yapısı (ogrenciNo, ogrenciAdi, ogrenciSoyad) şeklinde olsun.
#    ** öğrenci ekleme işlemi bittiğinde öğrencileri listeleyiniz.
devammi = "e"
ogrenciler = []

while devammi != "h" :
    ogrenciNo = input("Öğrenci no: ")
    ogrenciAd = input("Öğrenci ad: ")
    ogrenciSoyad = input("Öğrenci soyad: ")

    ogrenciler.append({
        "ogrenciNo" : ogrenciNo,
        "ogrenciAd" : ogrenciAd,
        "ogrenciSoyad" : ogrenciSoyad
    })

    devammi = input("devam mı? (e/h): ")

for ogrenci in ogrenciler : 
    print(f"{ogrenci['ogrenciNo']} numaralı öğrencinin adı {ogrenci['ogrenciAd']} {ogrenci['ogrenciSoyad']}")