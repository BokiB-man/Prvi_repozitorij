import random



# a = 10
# b = 5

# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a ** 2)


# print(10 % 3)


# godine = 25

# godine = godine + 1

# godine += 1

# print(godine)

# godine *= 2

# print(godine)

# broj1 = int(input("Unesite prvi broj:"))
# broj2 = int(input("Unesite drugi broj:"))

# print("Zbir:", broj1 + broj2)

# poluprecnik = float(input("Unesite poluprecnik:"))
# pi = 3.14

# povrsina = poluprecnik ** 2 * pi

# print("Povrsina kruga je:", povrsina)


# unos = input("Unesi nesto...")

# print(unos.isnumeric())




# stara_kilaza = 80
# nova_kilaza = 90

# print(stara_kilaza < nova_kilaza)
# print(stara_kilaza > nova_kilaza)
# print(stara_kilaza == nova_kilaza)
# print(stara_kilaza != nova_kilaza)


# username = "test"
# password = "abc123"

# print(username == "test")
# print(password == "abc123")


# broj = int(input("Unesite broj:"))

# provera = broj % 2
# print("Paran broj?", provera ==0)



# korisnik = int(input("Unesite neki broj:"))
# racunar = random.randint(1, 10)

# print("Korisnik:", korisnik)
# print("Racinar:", racunar)
# print("Pogodak:", korisnik == racunar)






# automobil = 0
# cilj = 50

# print(automobil >= cilj)
# automobil += 50
# print(automobil >= cilj)





provera_imena = True
provera_sifre = False

print(provera_imena or provera_sifre)

'''
and

true true => True
true false => False
false true => False


or

true true => True
true false => True
false false => False
'''


kurs = input("Unesite kurs:")
generacija = int(input("Generacija:"))

odobreno = kurs == "python" and generacija == 2022
print(odobreno)




