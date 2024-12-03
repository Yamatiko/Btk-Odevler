a, b, c = 4, 8, (12, 2)

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile a,b,c toplamının farkı nedir?

# sayi1 = int(input("1. sayıyı girin: "))
# sayi2 = int(input("2. sayıyı girin: "))
# sonuc1 = sayi1 * sayi2 - (a+b+sum(c))

# 2- c' nin b' ye kalansız bölümünü hesaplayınız.
sonuc2 = sum(c)//b


# 3- (a,b,c) toplamının mod 7' si nedir?
sonuc3 = (a+b+sum(c)) % 7

# 4- b' nin a. kuvvetini hesaplayınız.
sonuc4 = b ** a

# 5- a, *b, c = (2,4,6,8,13) işlemine göre c' nin küpü nedir?
a = 2
b = [4, 6, 8]
c = 13

sonuc5 = c ** 3

# 6- a, b, *c = (2,4,6,8,13) işlemine göre c' nin değerleri toplamı nedir?
a = 2
b = 4
c = [6,8,13]
sonuc6 = sum(c)

print(sonuc6)