import requests
from bs4 import BeautifulSoup
## import the scraper
import os
import time

def clear():
    if os.name == 'nt':  # Windows
        _ = os.system('cls')
    else:  # Linux or macOS
        _ = os.system('clear')

def find_word_and_get_link(url, the_word):
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    
    # Find all links on the page
    links = soup.find_all('a', href=True)
    
    # Search for the specified word in each link's text
    for link in links:
        if the_word in link.text:
            return link['href']
    
    return None
    ## scrapes for the thing
def main():
    clear()
    print("PLUMAN v1")
    print("By VPeti")
    time.sleep(1)
    pluginname = input("What plugin? ")
    url = 'https://dev.bukkit.org/projects/' + pluginname + '/files'
    ## devbukkit url here (ALL FILES)
    word = input("What version? ")
    ## version here
    download_link = find_word_and_get_link(url, word)
    web = 'https://dev.bukkit.org'
    web2 = '/download'
    
    if download_link:
        dl = web +  download_link + web2
        print(f"Download link found! ({dl})")
        os.system("wget " + dl + " -O" + pluginname + ".jar")
        print("Plugin downloaded. Restarting the program")
        time.sleep(1)
        main()

    else:
        print(f"{word} not found. Restarting the program")
        time.sleep(2)
        main()

if __name__ == '__main__':
    main()

   