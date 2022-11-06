import json
import difflib
# data = {
#     'name' : "Bola",
#     'age' : 24,
#     'favorit_food' : ['Rice', 'Bread', 'Beans']
# }
data = json.load(open('english_dictionary.json', 'r'))
print("Type a word you want to search")
word = input("")
if len(word) < 1:
    print("You did not type a word, please type a word")
if word not in data.keys():
    print("Please do you mean ny of these words below")
    print(difflib.get_close_matches(word, data, 5))
    result = input("")
    print(data[result])
else:
    print(data[word])
