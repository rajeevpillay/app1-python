import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]

    elif len(get_close_matches(word.lower(),data.keys()))>0:
        yn=input("Did you mean %s instead. If yes press Y,else press N. " % get_close_matches(word,data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        #    translate(get_close_matches(word,data.keys())[0])

        elif yn=="N" :
            return "Word does not exist."

        else:
            return "We did not understand your query."

    else:
        return "Word does not exist."

word = input("Enter word: ")
output = translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
