import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://openlibrary.org' + '/search?q=ddc%3A8%2A+first_publish_year%3A%5B%2A+TO+1950%5D+publish_year%3A%5B2000+TO+%2A%5D+NOT+public_scan_b%3Afalse+language%3Arus+-subject%3A"content_warning%3Acover"+-subject%3A"content_warning%3Acover"&sort=trending'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36'
    }
    cookies = {'donation-identifier': 'MC4xMDI3NDQ3MTc5NDc2MzA5Ng=='}
    response = requests.get(url, headers=headers, cookies=cookies)

    if response.status_code != 200:
        print(f"Ошибка: {response.status_code}")
        return
    if "Verification failed. Please try again." in response.text:
        print("Verification failed")
        return
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.prettify())


if __name__ == "__main__":
    main()
