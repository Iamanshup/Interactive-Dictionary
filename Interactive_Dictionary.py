import json
from difflib import get_close_matches

data = json.load(open('data.json','r'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        reply = input("Did you mean %s instead? Enter Y if yes, or N if no: " %get_close_matches(word, data.keys())[0])
        if reply == 'Y' or reply == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif reply == 'N' or reply == 'n':
            return "The word does not exist. Please double check it."
        else:
            return "We did not understand you answer."
    else:
        return "The word does not exist. Please double check it."

meaning = translate(input("Enter a word: "))

if type(meaning) == list:
    for i in meaning:
        print(i)
else:
    print(meaning)
