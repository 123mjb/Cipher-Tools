import string
import sys


def rotate_character(c, rot):
    if c in string.ascii_lowercase:
        start = ord('a')
        return chr((ord(c) - start + rot) % 26 + start)
    elif c in string.ascii_uppercase:
        start = ord('A')
        return chr((ord(c) - start + rot) % 26 + start)
    else:
        return c

def rotate_string(s, rot):
    return ''.join(rotate_character(c, rot) for c in s)

def main(inputfile=None,outputfile=None):
    clear_outputfile(outputfile)
    if inputfile:
        with open(inputfile, 'r') as f:
            text = f.read()
    else:
        text = "Hello, World!"
    output_results(outputfile,"Original:\n"+ text)
    for i in range(1, 26):
        output_results(outputfile,f"\nROT-{i}:\n"+ rotate_string(text, i))

def output_results(outputfile, out):
    if outputfile:
        with open(outputfile, 'a') as f:
            f.write(out)
    else:
        print(out)
def clear_outputfile(outputfile):
    if outputfile:
        with open(outputfile, 'w') as f:
            f.write("")

if __name__ == "__main__":
    inputfile = sys.argv[1] if len(sys.argv) > 1 else None
    outputfile = sys.argv[2] if len(sys.argv) > 2 else None
    main(inputfile, outputfile)