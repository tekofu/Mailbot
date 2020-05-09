# Port from https://github.com/zuzak/owo

"""MIT License

Original substitutions: Copyright (c) 2018 Eva (Nepeta)
JavaScript library:     Copyright (c) 2019 Douglas Gardner <douglas@chippy.ch>
Python library:         Copyright (c) 2019 tekofu

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

import random

owoPrefix = [
    '<3 ',
    'H-hewwo?? ',
    'HIIII! ',
    'Haiiii! ',
    'Huohhhh. ',
    'OWO ',
    'OwO ',
    'UwU '
]

owoSuffix = [
    ' :3',
    ' UwU',
    ' ʕʘ‿ʘʔ',
    ' >_>',
    ' ^_^',
    '..',
    ' Huoh.',
    ' ^-^',
    ' ;_;',
    ' ;-;',
    ' xD',
    ' x3',
    ' :D',
    ' :P',
    ' ;3',
    ' XDDD',
    ', fwendo',
    ' ㅇㅅㅇ',
    ' (人◕ω◕)',
    '（＾ｖ＾）',
    ' Sigh.',
    ' x3',
    ' ._.',
    ' (• o •)',
    ' >_<'
]

owoDict = {
    'r': 'w',
    'l': 'w',
    'R': 'W',
    'L': 'W',
    'no': 'nu',
    'has': 'haz',
    'have': 'haz',
    'you': 'uu',
    'the ': 'da ',
    'The ': 'Da '
}


def owo(owoInput):
    words = owoInput.split()
    for i in range(0, len(words)):
        word = words[i]
        if word in owoDict:
            words[i] = owoDict[word]
            owoInput = ' '.join(words)

    prefChoice = random.choice(owoPrefix)
    suffChoice = random.choice(owoSuffix)

    owoInput = owoInput.replace('l', 'w')
    owoInput = owoInput.replace('L', 'w')
    owoInput = owoInput.replace('r', 'w')
    owoInput = owoInput.replace('R', 'w')

    owoOutput = prefChoice + owoInput + suffChoice

    return owoOutput
