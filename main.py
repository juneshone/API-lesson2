import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import os



def shorten_link(token, url):
    bitly_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    data = {"long_url": url}
    response = requests.post(bitly_url, json=data,  headers={'Authorization': token})
    response.raise_for_status()
    bitlink = response.json().get('link')
    return bitlink

def count_clicks(token, link):
    parsed = urlparse(link)
    link = f'{parsed.netloc}{parsed.path}'
    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary'
    response = requests.get(bitly_url, headers={'Authorization': token})
    response.raise_for_status()
    clicks_count = response.json().get('total_clicks')
    return clicks_count

def is_bitlink(token, url):
    parsed = urlparse(url)
    link = f'{parsed.netloc}{parsed.path}'
    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}'
    response = requests.get(bitly_url, headers={'Authorization': token})
    return response.ok

def main():
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
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

# https://bit.ly/42reuxz

