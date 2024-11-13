# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 
# def my_func(kelime, tekrar) : 
#    return kelime * tekrar
# print(my_func("yaman ", 12))




# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
# def dikdortgen_alan(kenar1, kenar2) :
#    return kenar1*kenar2
# def dikdortgen_cevre(kenar1, kenar2) : 
#    return 2*(kenar1+kenar2)

# print(dikdortgen_alan(3,2))
# print(dikdortgen_cevre(3,2))

# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
# def yazitura() :
#     import random
#     list = ["Yazı", "Tura"]
#     return random.choice(list)
# print(yazitura())

# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
def aralarindaAsal(sayi1, sayi2) :
    asallar = []
    for sayi in range(sayi1,sayi2) :
        if sayi > 1 :
            for x in range(2, sayi) : 
                if sayi % x == 0:
                    break
            else :
                asallar.append(sayi)
            
                    
    print(asallar)    

aralarindaAsal(1,9)

# print(aradaki_asallar(10,23))

# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.
# tam_bolenler = []

# def tambolenbulma(sayi) :
#     for i in range(1, sayi+1) :
#         if sayi % i == 0 :
#             tam_bolenler.append(i)
#     print(tam_bolenler)

# tambolenbulma(20)