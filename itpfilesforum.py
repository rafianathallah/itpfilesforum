import string

def hapaxlegomenon():
    file = open("DawnoftheDemigods.txt","r")
    text = file.read().lower().replace("\n","")
    newtext = ""
    for character in text:
        if character not in string.punctuation:
            newtext += character
    text = newtext
    textlist = text.split(" ")
    dictionary = {}
    for word in textlist:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    newdictionary = []
    for word in dictionary:
        if dictionary[word] == 1:
            newdictionary.append(word)
    print("Hapaxes: ")
    for word in newdictionary:
        print(word)
        
hapaxlegomenon()