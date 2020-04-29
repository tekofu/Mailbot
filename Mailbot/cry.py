# Port from https://github.com/dead-bird/apcry/blob/master/api/cry.js

"""MIT License

Original Javascript:    Copyright (c) 2019 dead-bird
Python library:         Copyright (c) 2020 tekofu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import re
import random
import math

cryInput = "this is a sentence that i'm testing out"


def cry(cryInput):
    words = cryInput.lower()
    words = re.sub(r'\w+(ing)', rStrip, words)
    charList = list(words)
    chars = enumerate(charList)
    x = ""
    for index, item in chars:
        item = charPass(index, item)
        x = x + item
    return x

def rStrip(match):
    newRepl = match.group(0)[:-1]
    return newRepl

def chanceCheck(value):
    randomNum = random.random()
    chance = value >= randomNum
    return chance

def charPass(index, char):
    # Apostrophe -> semi-colon
    if char == "'" and chanceCheck(0.4):
        char = ";"
        if chanceCheck(0.5):
            char = char + char
        return char
    # Skip unfriendly characters
    if re.compile("[a-z0-9]").match(char) != None:
        return char
    # Swap with character ahead
    # TBA

    # Add random character
    if chanceCheck(0.49):
        char = randChar(char)
    # Add up to 3 random puncuations
    if chanceCheck(0.74):
        #for i in random.randrange(1, 3):
        char = char + ",, .;"[random.randrange(0,4)]
    # Clone character
    if chanceCheck(0.89):
        char = char + char
        return char
    # Delecte character
    if chanceCheck(0.99):
        return ""

def randChar(char):
    dict = "abcdefghijklmnopqrstuvwxyz,/'[]\\`"
    char = dict[math.floor(random.random() * len(dict))]
    return char
