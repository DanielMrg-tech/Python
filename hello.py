print("Hello World")
lista_ex = [1,2,3,4,5]
lista_ex2 = [6,7,8,9]
for i in range(len(lista_ex2)):
    lista_ex.append(lista_ex2[i])
    print(lista_ex)

lista_nr_comparare = [1,2,3,4,5,6,7,8,9,100,200,300,345,312,1312]

for i in range (len(lista_nr_comparare)):
    nr = lista_nr_comparare[i]
    if nr % 2 == 0:
        print("Nr nostru {} este par!".format(nr))
    else:
        print("Nr nostru {} este impar!".format(nr))


def inmulteste_cu_doi(un_nr):
    rezultat = un_nr * 2
    return rezultat
print(inmulteste_cu_doi(30))
r1 = inmulteste_cu_doi(30)
print(r1)

def extrage_nr_pare(lista1):
    lista_noua = []
    for i in range(len(lista1)):
        nr = lista1[i]
        if nr % 2 == 0:
            lista_noua.append(nr)
    return lista_noua

nr_extrase = extrage_nr_pare(lista_nr_comparare)
print(nr_extrase)