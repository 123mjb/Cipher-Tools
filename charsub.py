alphabet =    []
newalphabet = []


with open("./CipheredText.txt","r") as a:
    text = a.read()

with open("./ProcessedText.txt", "w") as a:
    for i in range(len(text)):
        try:
            a.write(str(newalphabet[alphabet.index(text[i].lower())]))
        except:
            a.write(text[i])