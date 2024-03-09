#set up a virtual environement 
python3 -m venv env
#activate the virtual env
source env/bin/activate

#if there is an error quit() then enter /Applications/Python\ 3.11/Install\ Certificates.command

#after pip install beautifulsoup one line at a time 
from urllib.request import urlopen
from bs4 import BeautifulSoup
page = urlopen("https://weimergeeks.com/examples/scraping/example1.html")
soup = BeautifulSoup(page, "html.parser")
print(soup.h1)

#caser l'élément dans un titre 
heading = soup.h1
print(heading.text)

#extraire le texte d'une liste 
city_list = soup.find_all( "td", class_="city" )
for city in city_list:
    print( city.get_text() )

#after pip install beautifulsoup + requests --> go to python environnement (python3) and...
from bs4 import BeautifulSoup
import requests
url = 'https://www.boxofficemojo.com/year/2018/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find( 'table' )

# get all the rows from that one table
rows = table.find_all('tr')
print(rows[1])

# get top 5 movies on this page - I know the first row is [1]
for i in range(1, 6):
    cells = rows[i].find_all('td')
    title = cells[1].text
    print(title)

#sur les 5 premières lignes du table, montrer les cells de colonnes 1, 2 et 6
for i in range(1, 6):
    cells = rows[i].find_all('td')
    print(cells[0].text, cells[1].text, cells[7].text)

#creer une liste décroissante en partant en 2019
years = []
start = 2019
for i in range(0, 10):
    years.append(start - i)
#avant de print, fermer les ... (faire enter)
print(years)

# create base url
base_url = 'https://www.boxofficemojo.com/year/'
#rajouter une année (présente dans la liste créée prcédemment) pour l'inclure à la fin de la base_url 
print( base_url + str(years[0]) + '/')

# Get previous link 
url = 'https://xkcd.com'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

#BS sélectionne tous les éléments <a> ayant un attribut "rel" égal à prev (qui renvoie donc à un lien précédent?), [0] to select the premier 
prevLink = soup.select('a[rel="prev"]')[0]
print(prevLink)
#verification 
print(prevLink.get('href'))

#ajouter ce href final pour trouver l'url particulier de ce comic
url = 'https://xkcd.com' + prevLink.get('href')
print(url)

#Maintenant ouvrir l'url
import webbrowser
webbrowser.open(url)

#Choper tous les urls, avec des conditions comme ne pas y inclure les files photos, puis mettre ces urls dans un document texte 
start = 'http://en.wikipedia.org/wiki/AnimalCrossing'
page = requests.get(start)
soup = BeautifulSoup(page.text, 'html.parser')

# name the text file that will be created or overwritten
filename = 'myfile.txt'

def capture_urls(filename, soup):
    # créé et ouvre la file myfile et y écrire 
    myfile = open(filename, 'w')

    # trouver tout le contenu de la page
    article = soup.find(id='mw-content-text')

    # select only <a> elements
    links_list = article.find_all('a')

    for link in links_list:
        if 'href' in link.attrs:
        #choisir que les liens dont les 6 premiers characters commencent par /wiki/
            if link.attrs['href'][:6] == '/wiki/':
            # eliminate Wikipedia photo and template links
                if link.attrs['href'][6:11] != 'File:' and link.attrs['href'][6:14] != 'Template':
                # write one href into the text file - \n is newline
                    myfile.write(link.attrs['href'] + '\n')

        # close and save the file after loop ends
    myfile.close()

# call the function et fait apparaître myfile.txt
capture_urls(filename, soup)