import json

from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w  in data:
        return data[w]
    elif w.title() in data:
        w=w.title()
        return data[w]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys(),cutoff=0.8)) > 0 or len(get_close_matches(w.title(),data.keys(),cutoff=0.8)) > 0 :
        choice=input("Did you mean %s instead ? Enter Y if yes or N if no" %get_close_matches(w,data.keys())[0])
        if choice.upper() == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif choice.upper() == "N":
            return "This word does not exist. Please double check."
        else:
            return "Invalid choice"
    else:
        return "This word does not exist. Please double check."
word=input("Enter word :")
meanings = (translate(word))
if type(meanings) == list:
    i = 1
    for meaning in meanings:
        print("%d. %s" %(i , meaning))
        i +=1
else:
    print(meanings)