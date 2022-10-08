# Calculates the mean for a given list
def CalcMean(meanList):
    meanSum = 0

    # Calculate the sum and count
    for curr in meanList:
        meanSum += curr

    return meanSum / len(meanList)


# Calculates the median for a given list
def CalcMedian(medianList):
    result = 0
    medianList.sort()

    # Check if list length is even or odd, if even then median is the mean of the middle 2 values
    if len(medianList) % 2 == 0:
        result = CalcMean([medianList[len(medianList) // 2], medianList[len(medianList) // 2 - 1]])

    else:
        result = medianList[len(medianList) // 2]

    return result


# Calculates mode for a given list
def CalcMode(modeList):
    return max(set(modeList), key=modeList.count)   # Returns most frequent element in list


if __name__ == '__main__':
    numList = [1, 2, 3, 4, 5]

    meanVal = CalcMean(numList)
    medianVal = CalcMedian(numList)
    modeVal = CalcMode(numList)

    print(f"Mean: { meanVal }")
    print(f"Median: { medianVal }")
    print(f"Mode: { modeVal }")
