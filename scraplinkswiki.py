from bs4 import BeautifulSoup
import requests
import re

# Fonction pour scrapper les liens vers les pages Wikipédia internes
def scrape_wikipedia_links(url):
    # Récupérer le contenu de la page
    page = requests.get('https://fr.wikipedia.org/wiki/Animal_Crossing')
    soup = BeautifulSoup(page.content, 'html.parser')

    # Trouver tous les liens dans la page
    links = soup.find_all('a', href=True)

    # Expression régulière pour correspondre aux liens Wikipédia internes. Le re est un module python permettant de déceler des patterns récurrents 
    wikipedia_link_pattern = re.compile(r'^/wiki/')

    # Filtrer les liens qui correspondent au modèle de lien Wikipédia interne
    internal_links = [link['href'] for link in links if wikipedia_link_pattern.match(link['href'])]

    return internal_links

# Exemple d'utilisation : scraper les liens internes de la page d'accueil de Wikipédia en anglais
wikipedia_homepage = 'https://en.wikipedia.org/wiki/Main_Page'
internal_links = scrape_wikipedia_links(wikipedia_homepage)

# Afficher les liens internes
for link in internal_links:
    print(link)

# Définition de la fonction pour écrire les liens dans un fichier texte
def write_links_to_file(links, filename):
    with open(filename, 'w') as file:
        for link in links:
            file.write(link + '\n')

# Exemple d'utilisation : écrire les liens dans un fichier texte
write_links_to_file(internal_links, 'wikipedia_links.txt')