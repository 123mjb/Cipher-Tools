alphabet =    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
newalphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


with open("./CipheredText.txt","r") as a:
    text = a.read()

with open("./ProcessedText.txt", "w") as a:
    for i in range(len(text)):
        try:
            a.write(str(newalphabet[alphabet.index(text[i].lower())]))
        except:
            a.write(text[i])