with open("./CipheredText.txt","r") as a:
    text = a.read()
frequency = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
realFreq = [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.16, 0.77, 4.0, 2.4, 6.7, 7.5, 1.9, 0.12, 6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074]

for i in text:
    index = ord(i.lower())
    if (index >= ord('a')) and (index <= ord('z')):
        index -= ord('a')
        frequency[index] += 1


alphabet =    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
newalphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

sorted_frequency, sorted_alphabet = zip(*sorted(zip(frequency, alphabet)))
sorted_realFreq, sorted_newalphabet = zip(*sorted(zip(realFreq, newalphabet)))

with open("./ProcessedText.txt", "w") as a:
    for i in range(len(text)):
        try:
            a.write(str(sorted_newalphabet[sorted_alphabet.index(text[i].lower())]))
        except:
            a.write(text[i])