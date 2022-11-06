from audioop import reverse
from itertools import count
from tkinter.font import names


class_mates_basic12 = ["kayode", "Tolu", "iyabo", "frank"]
class_mates_basic11 = ["Felix", "Nathabiel", "Stone", "Fruit"]

# class_mates_basic12.extend(class_mates_basic11[2:])

# print(class_mates_basic12)

# class_mates_basic12.remove("Kayode")
# print(class_mates_basic12)

# class_mates_basic12.pop()

# del class_mates_basic12[0]
# class_mates_basic12.clear()

# class_mates_basic12.sort(reverse = True)
# class_mates_basic12.sort(key = str.lower)


# print(class_mates_basic12)

# class_mates_basic12_duplicate = class_mates_basic12.copy()

# print(class_mates_basic12_duplicate)

# print([x for x in class_mates_basic12])

# name = []
# for x in class_mates_basic12:
#     name.append(x)

# print(name)

# name = list(class_mates_basic12)
# print(name)

best_friends = list(("Kayode", 1, "Tolu", "Tolu"))







# print(class_mates[-3:])
# class_mates[2] = "Daniel"

# class_mates[0] = ["Benjamin", "Ife"]

# print(class_mates)

# class_mates.append("Anu")
# print(class_mates)
# class_mates.insert(1, "Anu")
# print(class_mates)

#DICTIONARY

info_of_student = {
    "names" : ["Daniel", "Frank", "Bola", "Evelyn"],
    "age": [25, 24, 21],
    "class": "Basics 10",
    "height": [5, 4.4, 3.99, 5.5]

}

# print(info_of_student["age"][3])
# print(len(info_of_student))
# print(info_of_student.keys())
# print(info_of_student.items())

info_of_student["class"] = "Basic 11"

# print(info_of_student["class"])

for x in info_of_student["age"]:
    if x <  20  :
        print(x)


