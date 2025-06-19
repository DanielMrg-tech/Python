# write a program that receives from the console the following input
# 123124432, nume , varsta
# save this data to a list of people with cnp name age
from idlelib.debugger_r import restart_subprocess_debugger

list1 = []
example_man = {
    "CNP": 124124121,
    "Nane": "Daniel",
    "Age": 25
}

while True:
    input_text = input("Input data format: 123124123,daniel,32 \n")
    print(input_text.split(","))
    cnp, name, age = input_text.split(",")
    result_person = {
        "CNP": cnp,
        "Name": name,
        "Age": age
    }

    list1.append(result_person)
    for pers in list1:
        print(pers)