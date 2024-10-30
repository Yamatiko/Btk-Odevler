"""
Aşağıdaki müşterinin bilgilerini ve satın aldığı ürün bilgilerini değişkenler içerisinde saklayınız.
Toplam ödenen ücret nedir?
Ödenen miktarın kdv oranı nedir? (%18)

Sadık Turan
05321234567
info@sadikturan.com
Kocaeli

Satın Alınan Ürünler

Ürün adı: Kablosuz Mouse
Fiyatı: 550 TL

Ürün adı: Kablosuz Klavye
Fiyatı: 650 TL

Ürün adı: Dizüstü Bilgisayar
Fiyatı: 55.000 TL

"""
musteriAd = "Sadik"
musteriSoyad = "Turan"
musteriTelNo = "05321234567"
musteriEmail = "info@sadikturan.com"
musteriKonum = "Kocaeli"

fiyatKablosuzMouse = 550
fiyatKablosuzKlavye = 650
fiyatDizüstüBilgisayar = 55000

toplam = fiyatKablosuzMouse + fiyatKablosuzKlavye + fiyatDizüstüBilgisayar

kdv = toplam * 0.18

print(toplam)
print(kdv)