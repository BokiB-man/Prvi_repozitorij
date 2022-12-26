

# brojevi.sort()
# brojevi.reverse
# print(brojevi)






# brojevi = [9, 1, 3, 2, 5, 8, 7]

# sortirani_brojevi = [1, 2, 3, 5, 7, 8, 9]

# while True:
#     izvrsena_zamena = False
#     for i in range(1, len(brojevi)):
#         if brojevi[i] < brojevi[i-1]:
#             privremena = brojevi[i]
#             brojevi[i] = brojevi[i-1]
#             brojevi[i-1] = privremena
#             izvrsena_zamena = True
#     if izvrsena_zamena == False:
#         break
# print(brojevi)



# proizvod = ["Telefon", "Tv", "Kompjuter"]
# cena = [100, 200, 300]

# for i in range(len(proizvod)):
#         print(proizvod[i], cena[i])


# automobili = ["Audi", "BMW", "Yugo", "Citroen", "Kia", "Peugeot"]
# for i in range(len(automobili)):
#     if i == 5:
#         print("Ari vozi:", end=" ")
#     print(automobili[i])


proizvodi = [["Iphone 11", "Samsung S22", "Xiaomi X3"], ["MacBook Pro", "Acer", "Dell"], ["Ipad", "Samsung Galaxy Tab", "Xiaomi Tab"]]

telefoni = ["Iphone 11", "Samsung S22", "Xiaomi X3"]
laptopovi = ["MacBook Pro", "Acer", "Dell"]
tableti = ["Ipad", "Samsung Galaxy Tab", "Xiaomi Tab"]

# print(proizvodi[1][0])

# for kategorija in proizvodi:
#     for x in kategorija:
#         print(x)

# for i in range(len(proizvodi)):
    # print(proizvodi[i])
    # for j in range(len(proizvodi[i])):
    #     print(proizvodi[i][j])



# hrana = [
#               ["Cokolada", "Bombone", "Palacinke"],
#               ["Sarma", "Musaka", "Kiseli kupus"],
#               ["Pecena paprika", "Ajvar", "Sopska"]
#         ]

# for kategorija in hrana:
#     for jelo in kategorija:
#         print("Naziv:", jelo)
        # izlaz = f'''
        # <div style='1px solid red; background-color: gray;'>
        # {jelo}
        # </div>
        # '''

        # print(izlaz)
# ime = "Sofija"

# poruka = f"Cao {ime} !!!"
# print(poruka)

# a = 10
# b = 15
# sabiranje = f"Sabiranje brojeva {a} i {b} je {a+b}"
# print("Sabiranje brojeva:", sabiranje)




biblioteka = [ [ "Uvod u python", "Nepoznat autor", "123"], ["Uvod u racunare", "Aleksandra Lazarevic", "321"]]

biblioteka = []

while True:


    print("Odaberi komandu: 1-unos, 2-prikaz, 3-brisanje, > 3 izlaz")
    komanda = int(input("Unesite komandu: "))


    if komanda == 1:
        naslov = input("Unesite naslov: ")
        autor = input("Unesite autora: ")
        isbn = input("Unesite isbn: ")
        biblioteka.append([naslov, autor, isbn])
        print("Dodata knjiga")

    if komanda == 2:
        for knjiga in biblioteka:
            print(knjiga)


    if komanda == 3:
        kljucna_rec = input("Unesite naziv knjige za brisanje: ")
        for knjiga in biblioteka:
            for detalj in knjiga:
                if detalj == kljucna_rec:
                    biblioteka.remove(knjiga)
                    print("Knjiga je obrisana")

    if komanda > 3:
        print("Izlaz")
        break
