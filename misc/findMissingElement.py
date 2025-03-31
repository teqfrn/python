arr1 = [5,5,7,7]
arr2 = [5,7,7]
myDict = dict()

def findMissingElement(arr1, arr2):
    missingElement = None

    for x in arr1:
        if x in myDict: 
            myDict[x] += 1
        else: 
            myDict[x] = 1
    for x in arr2:
        myDict[x] -=1

    for x, val in myDict.items():
        if val != 0:
            missingElement = x
    return missingElement

print(findMissingElement(arr1, arr2))