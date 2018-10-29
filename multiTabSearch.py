import requests, sys, webbrowser, bs4, pyperclip

print('Googling...')
#TO DO---Launch search from command line(Kali)
if len(sys.argv) > 1:
    #Get search-term from command line
    search = ' '.join(sys.argv[1:])
else:
    #Get search-term from clipboard
    search = pyperclip.paste()
    
res = requests.get('https://www.google.com/search?q=' + search)
res.raise_for_status()

#This retrieves the returned top search result links
soup = bs4.BeautifulSoup(res.text)

#Opens a new tab for each result
linkElems = soup.select('.r a')
numb_Open = min(7, len(linkElems))
for i in range(numb_Open):
    webbrowser.open('https://www.google.com' + linkElems[i].get('href'))
