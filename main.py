from itertools import chain, combinations, permutations
from argparse import RawTextHelpFormatter
import argparse, random, re

ZERO_WIDTH_CHARS = [
    "‍",                    #   ZERO_WIDTH_JOINER
    "‌",                    #   ZERO_WIDTH_NONJOINER
    "​",                    #   ZERO_WIDTH_SPACE
    "⁠"                     #   ZERO_WIDTH_NOBREAK_SPACE
]

def decode(sec, oneChar, zeroChar, spaceChar):
    secBin = ""
    regex = re.compile("(‍|‌|​|⁠)")

    for match in regex.finditer(sec):
        if match == None:
            break
        char = match.group(0)
        if char == oneChar:
            secBin += "1"
        elif char == zeroChar:
            secBin += "0"
        elif char == spaceChar:
            secBin += " "

    if secBin == "":
        print("No zero-width characters were found.")
        exit()

    #   Check if the first and last character is a space, remove it if so.
    if (secBin[0] == " "):
        secBin = secBin[1:]
    if (secBin[len(secBin)-1] == " "):
        secBin = secBin[:len(secBin)-1]

    try:
        #   Convert the binary message into a string and return it.
        return ''.join([chr(int(x, 2)) for x in secBin.split(" ")])
    except Exception:
        return None

if __name__ == '__main__':
    #   Setup the Argument Parser.
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument("-s", "--secret", help="decode a secret message")
    parser.add_argument("-f", "--file", help="input a file to be decoded")
    parser.add_argument("-o", "--output", help="output results to a file")
    args = parser.parse_args()

    if args.secret == None and args.file == None:
        print("You have to either use --secret or --file.\nUse -h or --help for help")
        exit()

    if args.secret and args.file:
        print("How about no?")
        exit()

    decoded = []

    if args.secret:
        #   Go through all the permutations (basically combinations) of the zero-width characters.
        for comb in permutations(ZERO_WIDTH_CHARS, 3):
            decoded.append(decode(args.secret, comb[0], comb[1], comb[2]))

    if args.file:
        input = ""
        for line in open(args.file, "r", encoding="utf8").readlines():
            input += line

        for comb in permutations(ZERO_WIDTH_CHARS, 3):
            decoded.append(decode(input, comb[0], comb[1], comb[2]))

    if args.output:
        with open(args.output, "a", encoding="utf8") as f:
            for result in decoded:
                if result != None:
                    f.write("Decoded:\n"+ result +"\n\n")

    else:
        for result in decoded:
            if result != None:
                print("Decoded: " + result)
