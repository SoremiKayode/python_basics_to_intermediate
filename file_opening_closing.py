# f = open("C:\\Users\\kayodebarnabas.DESKTOP-N3C038F\\Documents\\essence_Hair.txt", "a")
# f.write("/n Tody is Sunday")

# f = open("C:\\Users\\kayodebarnabas.DESKTOP-N3C038F\\Documents\\essence_Hair.txt", "r")
# print(f.read())
# f.close()

# f = open("C:\\Users\\kayodebarnabas.DESKTOP-N3C038F\\Documents\\sunday.txt", "w")
# f.writelines("Tody is Sunday\n")
# f.writelines("Tomorrow is Monday\n")
# f.writelines("I am Going to school\n")
# f.writelines("On frdai i am travelling out of lagos\n")

# new_file =  open("C:\\Users\\kayodebarnabas.DESKTOP-N3C038F\\Documents\\sunday.txt", "r")
# print(new_file.read())

names_of_student = ["Bayo", "Bolu", "Daniel", "Frank", "Kate"]

for x in names_of_student:
    f = open(f"C:\\Users\\kayodebarnabas.DESKTOP-N3C038F\\Desktop\\file_list\\{x}.txt", "w")
    f.writelines(f"Congratulations!! {x}")
    f.writelines("\nYou've been given provision admission to Fruitful Ville")
    f.writelines("\nYou are to resume on Monday")
    f.writelines("\nSee you in school")


