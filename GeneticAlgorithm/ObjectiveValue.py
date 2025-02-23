def CalculateObjectiveValue(solution, mode):
    score = 0
    # Minimize sums of squares
    if mode == 1:
        for e in solution:
            score += e**2
    # One Max Problem or Absolute Value
    elif mode == 2 or mode == 3:
        score = sum(solution)
    else:
        exit("Modo Invalido")

    return score
