from itertools import chain, combinations, permutations
from argparse import RawTextHelpFormatter
import argparse, random, re

#   List for all the zero-width characters.
ZERO_WIDTH_CHARS = [
    "‍",                    #   ZERO_WIDTH_JOINER
    "‌",                    #   ZERO_WIDTH_NONJOINER
    "​",                    #   ZERO_WIDTH_SPACE
    "⁠"                     #   ZERO_WIDTH_NOBREAK_SPACE
]

#   Decode a secret with given zero-width characters.
def decode(sec, oneChar, zeroChar, spaceChar):
    #   Variable for binary of secret and regex for the characters.
    secBin = ""
    regex = re.compile("(‍|‌|​|⁠)")

    #   Get the matches in the secret and iterate over them.
    for match in regex.finditer(sec):
        #   If no matche were found, break out of the loop.
        if match == None:
            break

        #  Set the character to the current match.
        char = match.group(0)
        if char == oneChar:         #   If the character is the zero-width character for one.
            secBin += "1"
        elif char == zeroChar:      #   If the character is the zero-width character for zero.
            secBin += "0"
        elif char == spaceChar:     #   If the character is the zero-width character for space.
            secBin += " "

    #   If there is no binary, then no characters were found.
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
        #   Return nothing since it failed.
        return None

if __name__ == '__main__':
    #   Setup the Argument Parser.
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument("-s", "--secret", help="decode a secret message")
    parser.add_argument("-f", "--file", help="input a file to be decoded")
    parser.add_argument("-o", "--output", help="output results to a file")
    args = parser.parse_args()

    #   Check if NONE of the required arguments are used.
    if args.secret == None and args.file == None:
        print("You have to either use --secret or --file.\nUse -h or --help for help")
        exit()

    #   Check if BOTH of the arguments are used.
    if args.secret and args.file:
        print("How about no?")
        exit()

    #   List holding all the deocded results.
    decoded = []

    #   Check if we are passing in a string directly.
    if args.secret:
        #   Go through all the permutations (basically combinations) of the zero-width characters.
        for comb in permutations(ZERO_WIDTH_CHARS, 3):
            #   Decode the secret with the permutation.
            result = decode(args.secret, comb[0], comb[1], comb[2])

            #   Append it into the list if it isn't None.
            if result != None:
                decoded.append(result)

    #    Check if we are passing a file to parse.
    if args.file:
        #   Variable for holding the input of the file.
        input = ""

        #   Open the file and read all the lines, adding each of them to the input.
        for line in open(args.file, "r", encoding="utf8").readlines():
            input += line

        #   Go through all the permutations (basically combinations) of the zero-width characters.
        for comb in permutations(ZERO_WIDTH_CHARS, 3):
            #   Decode the secret with the permutation.
            result = decode(args.secret, comb[0], comb[1], comb[2])

            #   Append it into the list if it isn't None.
            if result != None:
                decoded.append(result)

    #    Check if we are going to write results to a file.
    if args.output:
        #   Open the file with UTF-8 encoding.
        with open(args.output, "a", encoding="utf8") as f:
            #   Iterate over the results and write it to the output file.
            for result in decoded:
                f.write("Decoded:\n"+ result +"\n\n")

    else:
        #   Iterate over the results and print it to CLI.
        for result in decoded:
            print("Decoded: " + result)
