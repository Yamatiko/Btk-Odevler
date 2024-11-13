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
# def asalSayimi(n) :
#      if n <= 1:
#         return False 
#      if n <= 3 :
#         return True
#      if n % 2 == 0 or n % 3 == 0 :
#         return False
#      i = 5 
#      while i * i <= n :
#          if n % i == 0 or n % (i+2) == 0 :
#              return False
#          i += 6
#      return True

# def aradaki_asallar(sayi1, sayi2) :
#     asallar = []
#     for sayi in range(sayi1, sayi2) :
#         if asalSayimi(sayi) == True :
#             asallar.append(sayi)
#     return asallar

# print(aradaki_asallar(10,23))

# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.
# tam_bolenler = []

# def tambolenbulma(sayi) :
#     for i in range(1, sayi+1) :
#         if sayi % i == 0 :
#             tam_bolenler.append(i)
#     print(tam_bolenler)

# tambolenbulma(20)