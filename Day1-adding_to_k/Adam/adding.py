def adding(numbers, sum):
    solutionList = []
    for i in range(len(numbers)):
        if numbers[i] in solutionList:
            return True
        solutionList.append(sum - numbers[i])
        if sum == numbers[i]:
            solutionList.append(0)
    return False


print(adding([10, 15, 3, 8, 234, 345, 6345, 234, 67, 391], 400))
