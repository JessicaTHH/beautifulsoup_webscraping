import requests
from bs4 import BeautifulSoup
from csv import writer

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name = "h3", class_ = "title")

with open('top100mustwatchmovies.csv', 'w') as file:
    thewriter = writer(file)
    header = ['Movies']
    thewriter.writerow(header)
# because you can't getText directly on a list, so here is using list comprehension.
    movie_titles = [movie.getText() for movie in all_movies]
    for n in range(len(movie_titles)-1, -1,-1):
      info = [movie_titles[n]]
      thewriter.writerow(info)

# or you can use slice operator
# movies = movie_titles[::-1]