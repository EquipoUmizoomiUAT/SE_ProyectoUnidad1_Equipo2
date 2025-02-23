import random
from CSV import ReadCSV


def GetInitialPopulation(populationSize, solutionSize, mode):
    # Get the whole dataset
    dataset = ReadCSV.ReturnDataSet(mode)
    population = []

    while len(population) < populationSize:
        # Get a random solution
        solution = dataset[random.randint(0, len(dataset) - 1)]

        # If the solutionSize is not 6, then adjust to the desired size
        if solutionSize != 6:
            solution = solution[:solutionSize]

        # Parse to integers
        solution = [int(i) for i in solution]

        # Save to Initial Population
        population.append(solution)

    return population
