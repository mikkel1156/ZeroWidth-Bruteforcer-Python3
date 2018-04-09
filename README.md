# Zero-Width Bruteforcer Python3
Based on my Zero-width character encoder/decoder, I wanted to make a bruteforcer using it. When I look around at what others have done, they don't use the same zero-width characters for *encoding* the bits as I do (as to be expected). So my encoding/decoding tool wouldn't necessarily help decoding something encoded with another tool.

This bruteforcing tool helps decode zero-width characters simply by giving it other input (permutations) to use as the representations of bits (and space), then returning the output it gets (at least one of them will be correct).

## Usage
```
usage: main.py [-h] [-s SECRET] [-f FILE] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -s SECRET, --secret SECRET
                        decode a secret message
  -f FILE, --file FILE  input a file to be decoded
  -o OUTPUT, --output OUTPUT
                        output results to a file
```