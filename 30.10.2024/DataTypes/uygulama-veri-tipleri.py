"""
    Uygulama 1: Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız.
    Alan: πr²
    Çevre: 2πr

    Uygulama 2: Klavyeden girilen km bilgisini mil cinsinden hesaplayınız.
    mil = km / 1.609344
"""
#Uygulama 1
r = float(input("Yarıçap girin: "))
pi = 3.14
daireAlan = pi*r**2
daireCevre = 2*pi*r

print(daireAlan)
print(daireCevre)

#Uygalama 2
km = float(input("Km giriniz: "))

mil = km / 1.609344

print("Uzunluğunuz mil cinsinden: ", round(mil, 2))