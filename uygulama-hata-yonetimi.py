liste = ["1","3","5","20b","abc","10a","60"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.

# mylist = []
# for i in liste :
#     try :
#         x =int(i)
#         mylist.append(x)
#     except ValueError as e:
#         print(e)
# print(mylist)

# 2: Kullanıcı 'quit (q)' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazın.
# while True:
#     mylist = []
#     x = input()
#     if x == "q" :
#         print(mylist)
#         break
#     try:
#         mylist.append(float(x))
#     except ValueError as e:
#         print(e)
#         continue
        
        
    


# 3: Dictionary ve key bilgilerini parametre olarak alan get(dict, key) fonksiyonu hazırlayınız.

urun = {"urunAdi":"samsung s20","fiyat":10000}

def get_urun(liste, key) :
    try:
        return liste[key]
    except KeyError :
        return None

print(get_urun(urun, "urunAdi"))


#  d["fiyat"] => KeyError

# get(urun, "fiyat")   => None
# get(urun, "urunAdi") => samsung S20

