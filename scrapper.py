import requests
from bs4 import BeautifulSoup

def fetch_anime_titles(anime_name):
    anime_name = anime_name.lower().replace(" ", "-")
    response = requests.get(f"https://www.animefillerlist.com/shows/{anime_name}")
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup)
    
    titles_elements = soup.find_all("td", class_="Title")
    titles = [title.get_text().strip() for title in titles_elements]
    # for title in titles:
    #     print(title.get_text().strip())
    
    return titles

if __name__ == "__main__":
    print(fetch_anime_titles("Naruto"))


