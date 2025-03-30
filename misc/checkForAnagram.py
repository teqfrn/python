phrase1 = 'Clint Eastwood'
phrase2 = 'old west action'

def checkForAnagram(phrase1: str, phrase2: str):
    """
    """
    phrase1 = ''.join(phrase1.lower().split(' '))
    phrase2 = ''.join(phrase2.lower().split(' '))

    anagram = dict()

    if len(phrase1) != len(phrase2):
        return False

    for x in phrase1:
        if anagram.get(x) is None:
            anagram[x] = 1
        else:
            anagram[x] += 1

    for x in phrase2:
        if anagram.get(x) is None:
            return False
        else:
            anagram[x] -= 1

    for x in anagram.values():
        if x != 0:
            return False
    return True

print(checkForAnagram(phrase1, phrase2))