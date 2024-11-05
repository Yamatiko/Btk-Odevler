# 1- Yaşı 18' den büyük ya da veli izni varsa bir işte çalışabilir durumunu kontrol ediniz.

# yas = int(input("Yaşınızı giriniz: "))
# veliIzni = bool(input("Veli izniniz varsa True yoksa False yazın: "))
# print(f"Çalışabilme: {yas > 18 or veliIzni == True}")

# 2- Ders notu 50-100 arasındaysa geçti değilse kalsın bilgisini yazdırınız.

# dersNotu = int(input("Notunuzu girin: "))
# if dersNotu <= 100 and dersNotu > 50 :
#     print("Geçtiniz!")
# else :
#     print("Seneye bekleriz :)")

# 3- Not ortalaması en az 70 puan ve zayıfı yoksa teşekkür belgesi alabilme durumunu kontrol ediniz.

# notlar = list(map(int, input("Notlarınızı giriniz: ").split()))
# notOrtalamasi = sum(notlar)/len(notlar)
# zayif = False

# if notOrtalamasi >= 70 and zayif == False :
#     print(notOrtalamasi)
#     print("Teşekkür belgesi aldınız.")
# else : 
#     print(notOrtalamasi)
#     print("Belge yalan oldu.")

# 4- İşe girmek için en az önlisans ya da lisans mezunu olma durumunu kontrol ediniz. Sigara kullanmama koşulu.

# egitimDurumu = input("Eğitim durumunuzu girin (önlisans, lisans): ")
# sigara = bool(input("Sigara kullanıyor musunuz? (True, False): "))
# print((egitimDurumu == "önlisans" or egitimDurumu == "lisans") and sigara)

# 5- Uygulamaya giriş kontrolünü "username yada email" ve "parola" için yapalım.

username = "yamatiko"
email = "tanyamantevfik@gmail.com"
parola = "Yaman12345"
emailinput = input("email girin: ")
usernameinput = input("username girin: ")
kontrol = (username == usernameinput or email == emailinput) and parola == input("parola girin: ")

print(kontrol)