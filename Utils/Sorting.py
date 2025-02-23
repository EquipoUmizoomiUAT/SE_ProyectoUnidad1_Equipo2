def QuickSort(solutions, scores):
    if len(scores) <= 1:
        return solutions, scores
    else:
        pivot = scores[len(scores) // 2]
        solutionsLeft, scoresLeft = [x for x in scores if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)