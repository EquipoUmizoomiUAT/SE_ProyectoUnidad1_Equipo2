import random


def Mutate(child, xMin, xMax, mutationChance):
    for i in range(len(child)):
        if random.random() < mutationChance:
            child[i] = random.randint(xMin, xMax)
    return child
