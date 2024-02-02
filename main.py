import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import os


def shorten_link(token, url):
    bitly_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    data = {"long_url": url}
    headers = {'Authorization': token}
    response = requests.post(bitly_url, json=data,  headers=headers)
    response.raise_for_status()
    bitlink = response.json().get('link')
    return bitlink


def count_clicks(token, link):
    parsed = urlparse(link)
    link = f'{parsed.netloc}{parsed.path}'
    headers = {'Authorization': token}
    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary'
    response = requests.get(bitly_url, headers=headers)
    response.raise_for_status()
    clicks_count = response.json().get('total_clicks')
    return clicks_count


def is_bitlink(token, url):
    parsed = urlparse(url)
    link = f'{parsed.netloc}{parsed.path}'
    headers = {'Authorization': token}
    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}'
    response = requests.get(bitly_url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    user_input = input('Введите ссылку: ')
    if is_bitlink(token, user_input):
        try:
            clicks_count = count_clicks(token, user_input)
            print('Количество кликов по ссылке за все дни', clicks_count)
        except requests.exceptions.HTTPError:
            print('Вы ввели неверную ссылку')
    else:
        try:
            bitlink = shorten_link(token, user_input)
            print('Битлинк', bitlink)
        except requests.exceptions.HTTPError:
            print('Вы ввели неверную ссылку!')


if __name__ == '__main__':
    main()
