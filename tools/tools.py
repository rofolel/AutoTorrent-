import string
import itertools
def get2letterString():
    strings = list()
    allTheLetters = string.lowercase
    return itertools.combinations(allTheLetters,4)
