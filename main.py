import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import os

load_dotenv()

token = os.environ['TOKEN']

def shorten_link(token, url):
    url_bitly = 'https://api-ssl.bitly.com/v4/bitlinks'
    data = {"long_url": url}
    response = requests.post(url_bitly, json=data,  headers={'Authorization': token})
    response.raise_for_status()
    bitlink = response.json().get('link')
    return bitlink

def count_clicks(token, link):
    link_parse = urlparse(link)
    link = link_parse.netloc + link_parse.path
    url_bitly1 = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary'
    response = requests.get(url_bitly1, headers={'Authorization': token})
    response.raise_for_status()
    clicks_count = response.json().get('total_clicks')
    return clicks_count

def is_bitlink(token, url):
    link_parse = urlparse(url)
    link = link_parse.netloc + link_parse.path
    url_bitly2 = f'https://api-ssl.bitly.com/v4/bitlinks/{link}'
    response = requests.get(url_bitly2, headers={'Authorization': token})
    return response.ok

def main():
    user_input = input('Введите ссылку: ')
    if is_bitlink(token, user_input):
        try:
            clicks_count = count_clicks(token, user_input)
        except requests.exceptions.HTTPError:
            print('Вы ввели неверную ссылку')  # если ошибка
        print('Количество кликов по ссылке за все дни', count_clicks(token, user_input))  # если все впорядке
    else:
        try:
            bitlink = shorten_link(token, user_input)  # пишется код, который потенциально может вызвать ошибку
        except requests.exceptions.HTTPError:
            print('Вы ввели неверную ссылку!')  # если ошибка
        print('Битлинк', shorten_link(token, user_input))  # если все впорядке

if __name__ == '__main__':
    main()


