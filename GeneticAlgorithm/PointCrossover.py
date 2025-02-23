import random
from GeneticAlgorithm import ObjectiveValue, Mutation


def PointCrossover(parentsVector, mutationChance, mode):
    # Prepare mutation range
    if mode == 1 or mode == 3:
        xMin, xMax = 0, 1023
    elif mode == 2:
        xMin, xMax = 0, 1
    else:
        exit("Invalid mode")

    children = []
    childrenScores = []
    parentIndex = 0

    while parentIndex < len(parentsVector):
        # Select a random point to cross over
        crossPoint = random.randint(0, len(parentsVector[0]) - 1)

        # Select two parents
        parent1 = parentsVector[parentIndex]
        parent2 = parentsVector[parentIndex + 1]

        # Create half of each child
        child1 = parent1[:crossPoint]
        child2 = parent2[:crossPoint]

        # Create the other half
        child1.extend(parent2[crossPoint:])
        child2.extend(parent1[crossPoint:])

        # Mutate each child
        child1 = Mutation.Mutate(child1, xMin, xMax, mutationChance)
        child2 = Mutation.Mutate(child2, xMin, xMax, mutationChance)

        # Add to children list
        children.append(child1)
        children.append(child2)

        # Calculate their scores and add them to a list
        childrenScores.append(ObjectiveValue.CalculateObjectiveValue(child1, mode))
        childrenScores.append(ObjectiveValue.CalculateObjectiveValue(child2, mode))

        # Advance to the next set of parents
        parentIndex = parentIndex + 2

    return children, childrenScores
