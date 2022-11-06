
name_of_student = {
    "name" : [],
    "age": [],
    "height" : [],
}

names_all = []
age_all = []
height_all = []

def printout():
    for x in range(2):
        print("Enter your name")
        name = input("")
        print("-----------------------------")

        print("Enter your age")
        age = int(input(""))
        print("-----------------------------")

        print("Enter your heigh in feet")
        height = float(input(""))
        print("-----------------------------")


        names_all.append(name)
        age_all.append(age)
        height_all.append(height)

        name_of_student["name"] = names_all
        name_of_student["age"] = age_all
        name_of_student["height"] = height_all


    print(name_of_student["name"])
    print(name_of_student["age"])
    print(name_of_student["height"])


printout()

# print(names_all)
# print(age_all)
# print(height_all)


