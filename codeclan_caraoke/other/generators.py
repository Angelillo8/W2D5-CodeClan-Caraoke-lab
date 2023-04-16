import requests
from bs4 import BeautifulSoup
import random
from classes.song import Song
from classes.guest import Guest

url = "https://singa.com/blog/best-karaoke-songs-of-all-time/"
html = requests.get(url)
html_soup = BeautifulSoup(html.content,"html.parser")
# print(html_soup.prettify())

songs = html_soup.find_all("strong")

songs_list = [i.get_text() for i in songs[1::]]
songs_list = [i.replace("\xa0", "") for i in songs_list[:-1:]]
songs_list = [i[3::] if i[0].isdigit() else i for i in songs_list]
songs_list = [i.replace("-"," – ").replace("—"," – ").replace("–"," – ").split(" – ") for i in songs_list]
songs_list = [i for i in songs_list if i != ['.']]

# print(songs_list)
# print(len(songs_list))

songs_dictionary = {}

for i in songs_list:
    songs_dictionary[i[0].strip()] = i[1].strip()

# print(songs_dictionary)

def song_generator(number_of_times):
    new_songs = []
    for i in range(number_of_times):
        song, artist = random.choice(list(songs_dictionary.items()))
        new_songs.append(Song(song,artist))
    return new_songs


url2 = "https://en.wiktionary.org/wiki/Appendix:Scottish_surnames"
html = requests.get(url2)
html_soup = BeautifulSoup(html.content,"html.parser")
# print(html_soup.prettify())

lastnames = html_soup.find_all("li")
lastnames = [i.get_text() for i in lastnames[22:-41]]
lastnames = [i.replace(", "," ").replace("/"," ").replace(" (also Frazer)", "") for i in lastnames]
lastnames = [i.split(" ") for i in lastnames]
lastnames = [j for i in lastnames for j in i]

url3 = "https://www.verywellfamily.com/50-scottish-baby-names-meanings-and-origins-5089418"
html = requests.get(url3)
html_soup = BeautifulSoup(html.content,"html.parser")
# print(html_soup.prettify())

firstnames = html_soup.find_all(class_="mntl-sc-block-heading__text")
firstnames = [i.get_text() for i in firstnames[2:]]
firstnames.remove(' Popular Scottish Baby Names for Boys\xa0 ')
firstnames = [i.replace("\xa0", "") for i in firstnames]
# print(firstnames)

def guest_generator(number_of_times):
    new_guests = []
    for i in range(number_of_times):
        new_guests.append(Guest(random.choice(firstnames) + random.choice(lastnames), 
                        random.choice(list(songs_dictionary.keys())), random.randint(16,250)))
    return new_guests

# print(guest_generator())