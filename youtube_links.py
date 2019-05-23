from bs4 import BeautifulSoup
import requests

youtube_link = 'https://www.youtube.com'
search_link='https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH'


data = requests.get(search_link, timeout=3)

soup = BeautifulSoup(data.text, 'lxml')

attr = {
    'class' : 'yt-uix-scroller-scroll-unit vve-check currently-playing'
}
current_link =  soup.find('li', attrs = attr)
print(youtube_link + current_link.a['href'])

attr = {
    'class' : "yt-uix-scroller-scroll-unit vve-check"
}

links = soup.find_all('li', attrs = attr)
for link in links:
    print(youtube_link + link.a['href'])


