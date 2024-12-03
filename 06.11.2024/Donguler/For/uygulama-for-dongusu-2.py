urunler = [
    {"urunAdi":"Hp Victus 1", "fiyat": 32999},
    {"urunAdi":"Lenovo ThinkPad", "fiyat": 25499},
    {"urunAdi":"Apple Macbook", "fiyat": 49999},
    {"urunAdi":"Huawei Matebook", "fiyat": 26999},
    {"urunAdi":"Casper Nirvana", "fiyat": 20000},
    {"urunAdi":"Hp Victus 2", "fiyat": 30000},
]

# 1- Aşağıdaki örnek cümleyi tüm ürünlere uygulayınız.
#    "Hp Victus marka ürünün fiyatı 32999 Türk Lirası."

# for urun in urunler :
#     print(f"{urun['urunAdi']} marka ürünün fiyatı {urun['fiyat']} Türk Lirasıdır.")
    

# 2- Ürünlerin fiyatları toplamı nedir?
# toplam = 0
# for urun in urunler :
#     toplam += urun['fiyat']
# print(toplam)

# 3- 25000 ile 40000 arasındaki ürünleri listeleyiniz.
# list = []
# for urun in urunler : 
#     if 25000 < urun['fiyat'] < 40000 :
#         list.append(urun['urunAdi'])
# print(list)
        
# 4- Kullanıcıdan alınan anahtar kelimeye göre ürünleri listeleyiniz.

kelime = input("Aramak istediğiniz ürün: ")

for urun in urunler : 
    if urun["urunAdi"].lower().find(kelime.lower()) > -1 :
        print(f"{urun['urunAdi']}")