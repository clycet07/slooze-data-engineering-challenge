import requests
from bs4 import BeautifulSoup
import json
import time
import random

BASE_URL = "https://dir.indiamart.com/impcat/cnc-machines.html"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_product_links(url):

    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("div", class_="lst")

    links = []

    for product in products:

        title = product.find("span", class_="pn")
        price = product.find("span", class_="prc")
        company = product.find("span", class_="cpn")
        location = product.find("span", class_="loc")

        data = {
            "product_name": title.text if title else None,
            "price": price.text if price else None,
            "supplier": company.text if company else None,
            "location": location.text if location else None
        }

        links.append(data)

    return links


def run_crawler(pages=5):

    all_data = []

    for page in range(1, pages+1):

        print(f"Scraping page {page}")

        url = BASE_URL + f"?page={page}"

        data = get_product_links(url)

        all_data.extend(data)

        time.sleep(random.uniform(2,5))

    with open("../data/raw/products.json", "w") as f:

        json.dump(all_data, f, indent=4)

    print("Data saved.")


if __name__ == "__main__":

    run_crawler()
