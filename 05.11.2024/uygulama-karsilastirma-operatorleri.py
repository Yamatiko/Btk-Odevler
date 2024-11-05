# 1- Girilen 2 sayıdan hangisi büyüktür?

# sayi1 = int(input("1. sayıyı girin: "))
# sayi2 = int(input("2. sayıyı girin: "))
# if sayi1 >= sayi2 :
#     print("Bu sayı daha büyük:", sayi1)
# elif sayi1 <= sayi2 :
#     print("Bu sayı daha büyük:", sayi2)


# 2- Girilen bir sayının tek çift kontrolünü yapınız.

# sayi3 = int(input("Bu sayı tek mi çift mi: "))
# if sayi3 % 2 == 0 :
#     print("Çift!")
# else :
#     print("Tek!")

# 3- Bir öğrencinin girilen 3 notuna göre başarı durumunu kontrol ediniz. 50 ve üstünde başarılı.
not1 = int(input("1. notunuzu giriniz: "))
not2 = int(input("2. notunuzu giriniz: "))
not3 = int(input("3. notunuzu giriniz: "))

notlar = (not1, not2, not3)

if sum(notlar)/len(notlar) >= 50 :
    print("Başarılısın!")
else :
    print("Daha çok çalışmalısın!")