def Selection(populationVector, scoresVector, populationSize, mode):
    # Combine lists to sort by score
    combined = list(zip(scoresVector, populationVector))

    # Minimization
    if mode == 1 or mode == 3:
        combined.sort()
        combined = combined[:populationSize]

    # Maximization
    elif mode == 2:
        combined.sort(reverse=True)
        combined = combined[:populationSize]

    else:
        exit("Invalid mode")

    # Regain selected population
    scoresVector, populationVector = zip(*combined)

    return list(populationVector), list(scoresVector)
