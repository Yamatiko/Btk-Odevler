# Not Uygulaması

# 1- Menu 
    # 1- Not Gir
    # 2- Ortalamaları Göster 
    # 3- Notları Kayıt Et
    # 4- Çıkış

    # 90-100 -> AA 
    # 80-89  -> BA 
    # 75-79  -> BB
    # 70-74  -> CB
    # 65-69  -> CC
    # 60-64  -> DC
    # 50-59  -> DD
    # 40-49  -> FD
    # 0 -39  -> FF

def notGir() :
    ad = input("Öğrenci ad: ")
    soyad = input("Öğrenci soyad: ")
    not1 = input("Not 1: ")
    not2 = input("Not 2: ")
    not3 = input("Not 3: ")

    with open("sinav_notlari.txt", "a", encoding = "utf-8") as file :
        file.write(ad + ' ' + soyad + ': ' + not1 + ', ' + not2 + ', ' + not3 + '\n')

def notlariOku() :
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file :
        for satir in file :
            print(not_hesapla(satir))
        

def not_hesapla(satir) :
    satir = satir[:-1]
    liste = satir.split(":")

    ogrenci_adi = liste[0]
    notlar = liste[1].split(",")
    
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    
    ortalama = (not1 + not2 + not3) / 3
    if 90 <= ortalama <= 100 :
        harf = 'AA' 
    elif 85 <= ortalama <= 89 :
        harf = 'BA' 
    elif 80 <= ortalama <= 84 :
        harf = 'BB' 
    elif 75 <= ortalama <= 79 :
        harf = 'CB' 
    elif 70 <= ortalama <= 74 :
        harf = 'CC' 
    elif 65 <= ortalama <= 69 :
        harf = 'DC' 
    elif 60 <= ortalama <= 64 :
        harf = 'DD' 
    elif 55 <= ortalama <= 59 :
        harf = 'ED' 
    elif 50 <= ortalama <= 54 :
        harf = 'EE' 
    elif 0 <= ortalama <= 49 :
        harf = 'FF' 
    
    return f"{ogrenci_adi}: {harf} - ({round(ortalama, 2)})"

def notKaydet() :
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file :
        myliste = []

        for satir in file :
            myliste.append(not_hesapla(satir))
        
        with open("sonuclar.txt", "w", encoding="utf-8") as file2:
            file2.writelines(myliste)

while True :
    secim = input('''
1- Not Gir
2- Notları Göster 
3- Notları Kayıt Et
4- Çıkış
''')
    if secim == "1" :
        notGir()
    elif secim == "2" :
        notlariOku()
    elif secim == "3" :
        notKaydet() 
    elif secim == "4" :
        break
    else :
        print("Yanlış tuşladınız.")
        print("\n")