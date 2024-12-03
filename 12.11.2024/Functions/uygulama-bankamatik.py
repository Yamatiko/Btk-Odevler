# Bankamatik Uygulaması

# Hesap bilgileri tutulacak. (dict)
# menu, paraCekme, bakiyeSorgula, paraYatirma fonksiyonları tanımlanacak.
# çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.

hesaplar = [
    {
        "ad":"Sadık Turan",
        "hesapNo": "12345",
        "bakiye": 20000,
        "ekHesap": 5000,
        "username":"sadikturan",
        "password":"1234"
    },
    {
        "ad":"Efe Turan",
        "hesapNo": "12345",
        "bakiye": 30000,
        "ekHesap": 10000,   
        "username":"efeturan",
        "password":"1234"
    }
]

def menu(hesap) :
    
    

    print("1- Bakiye sorgulama")
    print("2- Para çekme")
    print("3- Para Yatırma")

    islem = input("Yapmak istediğiniz işlem: (1-2-3) ")

    if islem == "1" : 
        bakiyeSorgulama(hesap)
    elif islem == "2" :
        paraCekme(hesap) 
    elif islem == "3" :
        paraYatirma(hesap)  
    else :
        print("Yanlış tuşladınız")
        menu(hesap)

    


def bakiyeSorgulama(hesap) :
    print("\n")
    print(f"Bakiye: {hesap['bakiye']}")
    print("\n")
    menu(hesap)

def paraCekme(hesap) :
    print("\n")
    miktar = int(input("Çekmek istediğiniz miktarı giriniz: "))
    print("\n")
    if miktar <= hesap['bakiye'] :
        print(f"Çektiğiniz miktar: {miktar}, kalan: {hesap['bakiye'] - miktar}")
        print("\n")
    elif miktar > hesap['bakiye'] :
        print("Limitiniz yetersiz")
        print("\n")
        ekHesapIzni = input("Ek hesabınızı kullanmak ister misiniz? (e/h)")
        print("\n")
        if ekHesapIzni == "e" :
            hesap['bakiye'] += hesap['ekHesap']
            print(f"Çektiğiniz miktar: {miktar}, kalan: {hesap['bakiye'] - miktar}")
            print("\n")
            if hesap['bakiye'] + hesap['ekHesap'] < miktar :
                print("Ek hesabınız da yetersiz.")
                print("\n")
        elif ekHesapIzni == "h" : 
            print("Üzgünüz işleminizi gerçekleştiremiyoruz.")
            print("\n")
    menu(hesap)
        
    


def paraYatirma(hesap) :
    print("\n")
    seciliHesap = input('''Hangi hesaba yatırım yapmak istiyorsunuz? (1/2)
1- Ana Hesap
2- Ek Hesap
''')
    yatirilanPara = int(input("Yatırılan miktarı giriniz: "))
    if seciliHesap == "1" :
        hesap['bakiye'] += yatirilanPara
        print(f"İşlem sonucu ana hesabınız: {hesap['bakiye']}, ek hesabınız: {hesap['ekHesap']}")
    elif seciliHesap == "2" :
        hesap['ekHesap'] += yatirilanPara
        print(f"İşlem sonucu ana hesabınız: {hesap['bakiye']}, ek hesabınız: {hesap['ekHesap']}")
    
    



def login() :
    username = input("Username: ")
    password = input("Password: ")

    isLoggedIn = False
    for hesap in hesaplar : 
        if hesap["username"] == username and hesap["password"] == password :
            isLoggedIn = True
            print("\n")
            print(f"Hoş geldin {hesap['ad']}")
            menu(hesap)
            break
            
    if not (isLoggedIn) :
        print("Username ya da parola hatalı.")


login()
    