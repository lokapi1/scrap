from bs4 import BeautifulSoup
import requests

# links from http://en.wikipedia.org/wiki/Harrison_Ford
link_list = ['/wiki/Animal-Crossing',
    '/wiki/Tom_Nook',
    '/wiki/Mr._Resetti']

# harvest data from each URL
def get_info(page_url):
    page = requests.get('https://en.wikipedia.org' + page_url)
    soup = BeautifulSoup(page.text, 'html.parser')

    try:
        print(soup.h1.get_text())
        # get all paragraphs in the main article
        paragraphs = soup.find(id='mw-content-text').find_all('p')
        for p in paragraphs:
            # skip any paragraph that has attributes
            if not p.attrs:
                # print 280 characters from the first real paragraph on the page
                print( p.text[0:280] )
                break
        print() # blank line
    except:
        print(page_url + ' is missing something!')

# call the function for each URL in the list
for link in link_list:
    get_info(link)