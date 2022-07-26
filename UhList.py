
larger = [1, 2, 3, 616]

smaller = [616]

def isSublist():
    for i in range(0, len(larger)):
        if larger[i:i + len(smaller)] == smaller:
            return True
    return False
print(isSublist())