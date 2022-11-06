import json
import difflib
data = json.load(open('english_dictionary.json', 'r'))

def check_word(search_query):
    if len(search_query) > 0:
        if search_query.lower() in data.keys():
            result = data[search_query]

            if type(result) == "list":
                 print("\n".join(result))
            else:
                print(result[0])
             
        else:
            alternative_words = difflib.get_close_matches(search_query, data, 5)
            print("Do you mean any of these words?")
            print("\n".join(alternative_words))
            print("You can search for any of the word above")
            word_search = input("")
            return check_word(word_search)
    else:
        print("Word to search must not be empty")
while True:
    print("Enter a word You want to search or press ! to quit")
    search_query = input("")
    if search_query == "!":
        break
    else:
        check_word(search_query=search_query)