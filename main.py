from GeneticAlgorithm import RunEvolution


if __name__ == "__main__":
    populationSize = 1000           # N Max 10k - Bigger get slower
    solutionSize = 6                # M Max 6 - Smaller gets faster
    mutationChance = 0.75           # T Apparently more mutation is worse
    generationAttempts = 10000      # G
    numberOfParents = populationSize // 2
    if numberOfParents % 2 == 1:
        numberOfParents += 1
    mode = 1
    RunEvolution.StartGenetic(populationSize, solutionSize, mutationChance, generationAttempts, numberOfParents, mode)
