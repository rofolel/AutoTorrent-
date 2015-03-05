import string
def get2letterString():
    strings = list()
    allTheLetters = string.lowercase
    for first in allTheLetters:
        for second in allTheLetters:
            strings.append('%s%s'%(first,second))

    return strings
