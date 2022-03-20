from random import random as getRandomNumber

def getNRandomNumbers(n,factorDeMultiplicacion):
    num = []
    for i in range (n):
        num.append(getRandomNumber() * factorDeMultiplicacion)

    return num