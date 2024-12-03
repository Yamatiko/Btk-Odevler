# 1- Faktöriyel fonksiyonu oluşturunuz ve fonksiyona gelen değer için hata mesajları verin.

def faktoriyel(i):
    i = int(i)
    if i < 0 :
        raise ValueError("Faktoriel negatif değer alamaz.")
    sonuc = 1
    for sayi in range(1, i+1) :
        sonuc *= sayi
    print(sonuc)
        
faktoriyel(3)

for i in [1,2,3,"ytt", 24,-3] :
    try :
        x = faktoriyel(i)
    except ValueError as ex :
        print(ex)
        continue
    else :
        print(x)

# 2- Girilen parola içinde türkçe karakter hatası veriniz.

def parola(x) :
    turkce_harfler = "şıöçüğİ"
    
    for i in x :
        if i in turkce_harfler:
            raise TypeError("Türkçe Harf kullandınız.")
    
    print("Geçerli parola.")


x = input("Parola: ")

try:
    parola(x)
except TypeError as e :
    print(e)

