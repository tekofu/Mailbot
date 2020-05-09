import re


def leet(leetInput):
    leetOutput = leetInput.upper()

    leetOutput = re.sub(r'\w+ER\b', xorSuff, leetOutput)
    leetOutput = re.sub(r'\w+OR\b', xorSuff, leetOutput)
    leetOutput = re.sub(r'\w+ED\b', edSuff, leetOutput)

    leetOutput = leetOutput.replace('AND', '&')
    leetOutput = leetOutput.replace('O', '0')
    leetOutput = leetOutput.replace('I', '1')
    leetOutput = leetOutput.replace('E', '3')
    leetOutput = leetOutput.replace('A', '4')
    leetOutput = leetOutput.replace('S', '5')
    leetOutput = leetOutput.replace('G', '6')
    leetOutput = leetOutput.replace('L', '7')

    return leetOutput


def xorSuff(match):
    newRepl = match.group(0)[:-2] + 'XOR'
    return newRepl


def edSuff(match):
    newRepl = match.group(0)[:-2] + '\'D'
    return newRepl