# 1- Başlangıç ve bitiş değerlerini kullanıcıdan alınız ve bu değerler arasındaki tüm çift sayıları yazdırınız.

# first = int(input("Write your initial number: "))
# last = int(input("Write your last number: "))
# while first < last :
#     if (first + 1) % 2 == 1 :
#         print(first)
#     first += 1

        


# 2- (1-100) arasındaki sayıları azalan şekilde yazdırınız.
# i = 99
# while i >= 1 :
#     print(i)
#     i -= 1

# 3- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.

# my_list = list(map(int, input("Enter 5 numbers separated by spaces: ").split()))

# my_list.sort()

# print(my_list)


# 4- Klavyeden girişi istenen username bilgisi için boşluk girildiği sürece tekrar username girişi isteyiniz.
username = ""
 
while not username :
    username = input("Enter your username: ")

print(f"The username is :{username}")
