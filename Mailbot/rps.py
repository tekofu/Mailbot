# Simple Rock Paper Scissors game
# Edited for Mailbot compliance

import random

toolList = ["ROCK", "PAPER", "SCISSORS"]


def inputOption(playerChoice):
    if playerChoice in toolList:
        return playerChoice
    else:
        errRps = None
        return errRps


def calculateWinner(playerChoice, compChoice):
    if playerChoice == compChoice:
        winningCond = "Draw"
        return winningCond
    elif playerChoice == "ROCK":
        if compChoice == "PAPER":
            winningCond = "Lose"
            return winningCond
        elif compChoice == "SCISSORS":
            winningCond = "Win"
            return winningCond
    elif playerChoice == "PAPER":
        if compChoice == "ROCK":
            winningCond = "Win"
            return winningCond
        elif compChoice == "SCISSORS":
            winningCond = "Lose"
            return winningCond
    elif playerChoice == "SCISSORS":
        if compChoice == "ROCK":
            winningCond = "Lose"
            return winningCond
        elif compChoice == "PAPER":
            winningCond = "Win"
            return winningCond


# Calculate the computer's play
def compChoice():
    compChoice = random.choice(toolList)
    return compChoice


# Print the final results
def finalMessage(playerChoice, compChoice, winningCond):
    rpsOutput = 'You picked ' + playerChoice + '. I picked ' + \
        compChoice + '. You ' + winningCond + '.'
    return rpsOutput
