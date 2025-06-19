import random

# sold = 1000
# def depunere():
#     suma = int(input("Adauga suma in lei "))
#     suma_bancomat = sold + suma
#     print(suma_bancomat)
# depunere()
#
# def retrage_suma():
#     retragere = int(input("Retrage suma dorita "))
#     if sold < retragere:
#         print("Bancomatul nu are suficienti bani ")
#     else:
#         suma_ramasa = sold - retragere
#         print(suma_ramasa)
#
# retrage_suma()
#
# def afisare_sold():
#     suma_aparat = sold
#     print(suma_aparat)
#
# afisare_sold()

# def filter_siruri(lista_siruri):
#     lista_pare = []
#     for sir in lista_siruri:
#         if len(sir) % 2 == 0:
#             lista_pare.append(sir)
#     return lista_pare
#
# siruri = ["Alin", "Mario", "Daniel", "Alex"]
# rezultat = filter_siruri(siruri)
# print(rezultat)

# sir_caractere = input("Introduceti un sir de caractere ")
#
# if sir_caractere.isdigit():
#     print("Sirul este un sir de numere ")
#     numar = int(sir_caractere)
#     if numar % 2 == 1:
#         print("Numarul este impar")
#     else:
#         print("Numarul este par")
# else:
#     print("Sirul este un sir de caractere")

# cetateni = {
#     19304843895738: {
#         "Nume": "Marius Moga",
#         "Varsta": 32,
#         "Adresa": "Brasov, Jud Brasov",
#         "Greutate": 75,
#     },
#     193048438345345: {
#         "Nume": "Matei Luca",
#         "Varsta": 26,
#         "Greutate": 59,
#     },
#     193048438345235: {
#         "Nume": "Matei Luca",
#         "Varsta": 22,
#         "Greutate": 59,
#     }
# }
#
# # def verifica_cetateni(cnp):
# #     cetatean = cetateni[cnp]
# #     if cetatean["Varsta"] > 25 and cetatean["Greutate"] < 60:
# #         print("Acesta indeplineste condiitle")
# #     else:
# #         print("Cetateanul nu indeplineste conditiile")
# #
# # print(verifica_cetateni(19304843895738))
#
# def verifica_cnp(cnp):
#     cetacean = cetateni[cnp]
#     if cetacean["Varsta"] > 25:
#         if cetacean["Greutate"] < 60:
#             print("Acest cetatean este valid")
#         else:
#             print("Cetateanul nu trece testul")
#     else:
#         print("Acest cetatean indeplineste doar o conditie")
#
# print(verifica_cnp(193048438345235))

# def joc_numere():
#     numar_secret = random.randint(1, 100)
#     while True:
#         try:
#             numar_utilizator = int(input("introdu un numar intre 1 si 100" ))
#             if numar_utilizator > numar_secret:
#                 print("Numarul introdus este prea mare, Incearca din nou! ")
#                 print(numar_secret)
#             elif numar_utilizator < numar_secret:
#                 print("Numarul introdus este prea mare, Incearca din nou! ")
#                 print(numar_secret)
#             else:
#                 print("Numarul introdus este bun, Felicitari!")
#                 print(numar_secret)
#                 break
#         except ValueError:
#             print("Introdu un numar corect ")
#
#
# while True:
#     joc_numere()
#     raspuns = input("Vrei sa joci din nou? da/nu"  ).strip().lower()
#     if raspuns != "da":
#         break
#
# def celsius():
#     grade = int(input("Introduceti gradele in celsius "))
#     conversie = grade * (9 / 5) + 32
#     print("Gradele in celsius sunt " + str(conversie))
#
# def fahrenheit():
#     grade2 = int(input("Introduceti gradele in fahrenheit "))
#     conversie2 = (grade2 - 32) * 5 / 9
#     print("Gradele in celsius sunt " + str(conversie2))
#
#
# alege_calculatorul = input("1. Celsius -> Fahrenheit 2. Fahrenheit -> Celsius ")
#
# if alege_calculatorul == "1":
#     celsius()
# elif alege_calculatorul == "2":
#     fahrenheit()

