import string
from _datetime import datetime
import random
# from tarfile import TruncatedHeaderError
from turtledemo.penrose import start

v = 10
def change(param1):
    param1 = 200

print(v)
change(v)
print(v)

l1 = [10, 20]

def change_list(list1):
    list1.append(30)

print(l1)
change_list(l1)
print(l1)

d1 = {
    "Name": "john",
    "age": 30
}

def change_dictionary(dict1):
    # dict1["employed"] = True
    dict1.update(employed=True)
print(d1)
change_dictionary(d1)
print(d1)

l1 = [1,2,3]
l1.append(4)
print(l1)

# s1 = "python"
# s1[0] = 't'

t1 = ("Brasov", 4000)
t2 = ("Iasi", 4000, True, "hundreds")
# t2[2] = False

print(t1)
print(t2[3])

v = {
    "nav_button": "closed",
    "cookie_banner": "active",
    "post_list": ["Why has America goes so far with it`s overweight?"],
    "user": "John",
    "users_active": 312412
}

# v["nav_button"] = "opened"
# v = {
#     "nav_button": "opened",
#     "cookie_banner": "active",
#     "post_list": ["Why has America goes so far with it`s overweight?"],
#     "user": "John",
#     "users_active": 312412
# }

list2 = [1,2,3,4,5,5,6,7,7,8,9,9,9,8,7]

set1 = set(list2)
print(len(set1))


list3 = []

for i in range(1000000):
    list3.append("".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)))

start = datetime.now()
print("ASDFG" in list3)
print("Stop: {}".format((datetime.now() - start).microseconds))
