import sys

myArr = []
desiredLen = 10

for i in range(desiredLen):
    """
    just checking how does the reference list grows in size
    every n elements to add extra room for new elements.
    """
    a = len(myArr)

    b = sys.getsizeof(myArr)

    myArr.append(i)

    print(f"length: {a} Size in bytes: {b}")
