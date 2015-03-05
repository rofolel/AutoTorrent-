import json
class film(object):
    def __init__(self,dic):

        for i in dic:
            self.__dict__[i] = dic[i]




def filmDB(object):
    films = list()