import requests
from bs4 import BeautifulSoup as bs


def find_chords(url):
    url_text = requests.get(url).text
    soup = bs(url_text, 'lxml')
    chords = soup.find(itemprop='chordsBlock')
    print(chords.text)


def find_song():
    search_url = 'https://amdm.ru/search/?q={}'
    song = input('Введите название песни(артиста): ')
    search_result = requests.get(search_url.format(song)).text
    soup = bs(search_result, 'lxml')
    if soup.body.article.h1.text == 'Ничего не найдено':
        return 'Ничего не найдено'
    song_list = soup.find_all('td', class_='artist_name')
    song_list = [(song.text, song.contents[2]['href']) for song in song_list]
    for number, name in enumerate(song_list):
        print(number, name[0])
    song_number = input('Введите номер песни: ')
    try:
        chords_url = 'http:' + song_list[int(song_number)][1]
        return find_chords(chords_url)
    except ValueError:
        return "Введена не цифра"


if __name__ == '__main__':
    find_song()
