from tqdm import tqdm
from GeneticAlgorithm import BinaryTournament, ObjectiveValue, PointCrossover, Population, Selection


def StartGenetic(populationSize, solutionSize, mutationChance, generationAttempts, numberOfParents, mode):
    populationVector = Population.GetInitialPopulation(populationSize, solutionSize, mode)
    scoresVector = []
    generation = 0
    score = -1

    if mode == 1 or mode == 3:
        # Minimization Problem
        for generation in tqdm(range(generationAttempts)):
            if score == 0:
                break
            scoresVector = [ObjectiveValue.CalculateObjectiveValue(e, mode) for e in populationVector]
            parentsVector = BinaryTournament.SelectParents(populationVector, scoresVector, numberOfParents, mode)
            childrenVector, childrenScores = PointCrossover.PointCrossover(parentsVector, mutationChance, mode)
            populationVector.extend(childrenVector)
            scoresVector.extend(childrenScores)
            populationVector, scoresVector = Selection.Selection(populationVector, scoresVector, populationSize, mode)
            score = min(scoresVector)

    elif mode == 2:
        # Maximization Problem
        for generation in tqdm(range(generationAttempts)):
            if score == solutionSize:
                break
            scoresVector = [ObjectiveValue.CalculateObjectiveValue(e, mode) for e in populationVector]
            parentsVector = BinaryTournament.SelectParents(populationVector, scoresVector, numberOfParents, mode)
            childrenVector, childrenScores = PointCrossover.PointCrossover(parentsVector, mutationChance, mode)
            populationVector.extend(childrenVector)
            scoresVector.extend(childrenScores)
            populationVector, scoresVector = Selection.Selection(populationVector, scoresVector, populationSize, mode)
            score = max(scoresVector)

    # Find the best solution and its score
    bestIndex = scoresVector.index(score)
    bestSolution = populationVector[bestIndex]

    print(f"Best Solution: {bestSolution}")
    print(f"Score: {score}")