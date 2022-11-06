

# student_age1 = 10

# ammount_to_pay = student_age1 * 50
# print(ammount_to_pay)

# student_age2 = 10

# ammount_to_pay = student_age1 * 50
# print(ammount_to_pay)

# def calculateStudentAge(name, age, height, **kwargs):
#     pass
# #     print("Your complexion is :" + kwargs["complexion"])

# calculateStudentAge("Bola", 27, 10.6, complexion = "Fair", favorite_subject = "Biology")

# c = lambda a, b : print(a * b)
# c(4, 6)

list_of_words = {
    "car" : "Aything you can drive",
    "House" : "A place where you live",
    "School" : "A place of leaning"
}

word = input("The word you want to search")

def check_word():
    if word in list_of_words.keys():
        print(list_of_words[word])

check_word()
