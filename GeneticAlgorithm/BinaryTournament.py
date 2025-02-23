import random


def SelectParents(populationVector, scoresVector, numberOfParents, mode):
    # Create parents vector
    parents = []

    for i in range(numberOfParents):
        # Get 2 random parents
        parent1 = random.randint(0, len(populationVector) - 1)
        parent2 = random.randint(0, len(populationVector) - 1)

        # Make sure they are different
        while parent1 == parent2:
            parent2 = random.randint(0, len(populationVector) - 1)

        # Minimization Problem
        if mode == 1 or mode == 3:
            # Compare their scores and see who is the best
            # Append the best to the parents vector
            if scoresVector[parent1] < scoresVector[parent2]:
                parents.append(populationVector[parent1])
            else:
                parents.append(populationVector[parent2])

        # Maximization Problem
        elif mode == 2:
            # Compare their scores and see who is the best
            # Append the best to the parents vector
            if scoresVector[parent1] > scoresVector[parent2]:
                parents.append(populationVector[parent1])
            else:
                parents.append(populationVector[parent2])
        else:
            exit("Invalid mode")

    # Return the parents vector
    return parents
