# for x in range(10):
#     for y in range(10):
#         if x < y:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()




automobil = 0
cilj = 100

brzina = 10
gorivo = 20
while automobil < cilj:
    print("Voznja u toku...")
    automobil += brzina
    gorivo -= 3
    if gorivo == 0:
        print("Nema goriva!") 
        break
else:
    print("Stigli ste!")