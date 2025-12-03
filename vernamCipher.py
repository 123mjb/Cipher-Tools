with open("./CipheredText.txt", "r") as a:
    text = a.read()

with open("./VernamKey.txt", "r") as a:
    key = a.read()

if len(text) == len(key):
    for i in range(len(text)):
        cChar = str(bin(text[i]))
        kChar = str(bin(key[i]))