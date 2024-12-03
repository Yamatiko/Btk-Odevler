sayilar = [3,5,7,2,12,32,45]

# 1- "sayilar" listesindeki her bir elemanı yazdırınız.

# for i in sayilar : 
#     print(i)


# 2- "sayilar" listesinde hangi sayılar 3' ün katıdır?

# for i in sayilar : 
#     if i % 3 == 0 :
#         print(i) 


# 3- "sayilar" listesinde tüm sayıların toplamı nedir?

# toplam = 0

# for i in sayilar :
#     toplam += i

# print(toplam)

urunler = ["iphone 13","samsung s24","samsung s22","iphone 15","iphone 14"]

# 4- "urunler" listesindeki tüm iphone marka ürünleri listeleyiniz. (find, index)
# for i in urunler :
#     index = i.find("iphone")
#     if index > -1 : 
#         print(i)


# 5- "urunler" listesinde kaç adet samsung ürünü vardır?
adet = 0
for i in urunler :
    index = i.find("samsung")
    if index > -1 : 
        adet += 1
        
print(adet)
