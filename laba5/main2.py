import requests
from bs4 import BeautifulSoup
from json import dumps


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36'
    }
    data = {}
    for i in range(50):
        url = f"https://books.toscrape.com/catalogue/page-{i+1}.html"
        print(f"page: {i+1}")
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Ошибка: {response.status_code}")
        soup = BeautifulSoup(response.text, "html.parser")
        for book in soup.find(class_="col-sm-8 col-md-9").ol.find_all("li"):
            title = book.h3.a['title']
            rating = 0
            for j in range(5):
                if ['One', 'Two', 'Three', 'Four', 'Five'][j] in book.p['class']:
                    rating = j + 1
                    break
            price = float(book.find(class_='product_price').p.string[2:])
            data[title] = {'rating': rating, 'price': price}
    with open('books.json', 'w') as file:
        file.write(dumps(data))


if __name__ == "__main__":
    main()
