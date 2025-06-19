# Ex. 1: Creaza functii de calcul aritmetic, + - * /, add, subtract, etc, si efectueaza urmatoarele calcule:
# 100 - 300 + (7 * 80) / 2
# 7 - 8 + 3 * 4 / 10


# Ex 2:
# Primind doua liste de date, de genul:

# Creaza o lista de dictionare, unde un element de dictionar arata:
# d = {
#     "Nume": "Matei",
#     "Varsta": 10
# }

# Ex 3:
# Primind lista: [10, 20, 80, 56, 2342, 5453, 7, 8 ,9]
# Folosind map(), ridica toate numerele la puterea a 2-a
# Creaza folosind filter() o lista cu toate nr pare din prima lista.

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def power(x, y):
    return x ** y

# print(100 - 300 + (7 * 80) / 2)
result = subtract(100, add(300, divide(multiply(7, 80), 2)))
# print(7 - 8 + 3 * 4 / 10)
result2 = subtract(7, multiply(add(8, 3), divide(4, 10)))
print(result2)
print(result)
# Inmulteste toate numerele de la 1 la 100

total = 1
for i in range(1, 101):
    total *= i

print(total)

list1 = [ 'Matei', 'Luca', 'Ana', 'Gabriel' ]
list2 = [ 10, 20, 30, 15 ]
#
# undifed = list(zip(list1, list2))
# print(undifed)
unified = []

for i in range(len(list1)):
    name = list1[i]
    age = list2[i]
    unified.append((name, age))


print(unified)