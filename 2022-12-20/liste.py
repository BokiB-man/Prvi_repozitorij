# osoba = ["Sofija", 25, "plava", False]

# for x in range(len(osoba)):
#     print(osoba[x])


# voce_i_povrce = ["jabuka", "beli luk", "crni luk", "banana", "mandarina", "lubenica", "krastavac"]

# for stavka in voce_i_povrce:
#     print(stavka)

# for x in range(len(voce_i_povrce)):
#     print("Na indeksu:", x, "Nalazi se:", voce_i_povrce[x])


# for x, vrednost in enumerate(voce_i_povrce):
#     print("Indeks:", x, "Stavka:", vrednost)





# automobili = ["Citroen", "BMW", "Opel", "Kia", "Yugo"]

# for pozicija, auto in enumerate(automobili):
#     if len(auto) == 3:
#         print(auto)
    # if auto == "Opel":
    #     print(pozicija, auto)
    # if pozicija == 1:
    #     print("Kupujem!")
    #     break
    # print("Pozicija:", pozicija, "Auto:", auto)

# automobili.append("Mercedes")

# print(automobili)

# del automobili[4]
# print(automobili)

# broj_opela = 0

# for x in range(len(automobili)):
#     if automobili[x] == "Opel":
#         print("Evo ga Opel")
#         broj_opela += 1

# print("Imam", broj_opela, "na placu.")


# automobili.clear()
# print(automobili)

# prazan_plac = []



# automobili = ["Citroen", "BMW", "Opel", "Kia", "Yugo", "Peugeot", "Audi"]


# automobili_akcija = []

# for x in range(len(automobili)):
#     if x == 1 or x == 2 or x == 3:
#         automobili_akcija.append(automobili[x])

# print(automobili_akcija)


# automobili_akcija = automobili[1:4]
# print(automobili_akcija)




a = [1,2,3,4,5,6,7,8,9]
parni = []
neparni = []

for x in a:
    if x % 2 == 0:
        parni.append(x)
    else:
        neparni.append(x)
print("Parni:", parni, "Neparni:", neparni)

# for x in a:
#     if x == 1 or x == 3 or x == 5 or x == 7 or x == 9:
#         print("Neparni:", x)
#     else:
#         print("Parni:", x)

