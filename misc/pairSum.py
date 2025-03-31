# pair_sum = ([1,3,2,2], 4)
# pair_sum = ([1,2,3,1], 3)
pair_sum = ([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1], 10)

def checkForPairs(pair_sum):
    elements = pair_sum[0]
    target = pair_sum[1]
    pairs = []

    for x in range(len(elements)):
        for y in range(x + 1, len(elements)):
            if (elements[x] + elements[y]) == target:
                pairs.append((min(elements[x], elements[y]), max(elements[x], elements[y])))

    return set(pairs)

def checkForPairsV2(pair_sum):
    elements = pair_sum[0]
    target = pair_sum[1]

    seen = set()
    output = set()

    if len(elements) < 2:
        return set()

    for num in elements:
        curr = target - num

        if curr not in seen:
            seen.add(num)
        else:
            output.add((min(num, curr), max(num, curr)))

    return output

print(checkForPairsV2(pair_sum))
