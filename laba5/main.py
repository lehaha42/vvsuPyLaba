import requests
from bs4 import BeautifulSoup


def main():
    url = "https://openlibrary.org"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.text)  # HTML-код страницы
    else:
        print(f"Ошибка: {response.status_code}")


if __name__ == "__main__":
    main()
