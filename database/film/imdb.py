import tools.tools
import requests
import film
import json

def getAllFilms():

    strings  = tools.tools.get2letterString()
    it = len(strings)/100
    incr = 0
    percent = 0
    films = list()
    print_s = '\rgetting IMdB database:  {0}%'

    print print_s.format(0)
    for i in strings:
        print '\rgetting IMdB database:{1}  {0}%     so far {2} films'.format(percent,i,len(films))
        incr += 1
        films += getFilmsWith(i)
        if incr > it :
            incr = 0
            percent += 1



def getFilmsWith(string):
    films = list()
    try:
        command = 'http://www.omdbapi.com/?s={0}&y=&plot=short&r=json'.format(string)
        r = requests.get(command)
        jsonstring =  r.text
        jsonstring = json.loads(jsonstring)

        for i in jsonstring["Search"]:
                _film = film.film(i)
                films.append(film)
    except:
        pass
    return films







def getAllSeries():
    pass
def getSeriesEpisodes():
    pass