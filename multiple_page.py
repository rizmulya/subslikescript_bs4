from bs4 import BeautifulSoup
import requests

root = "https://subslikescript.com"
web = f"{root}/movies"
print(f"GET {web}")
res = requests.get(web)
content = res.text
soup = BeautifulSoup(content, "html.parser")

article = soup.find("article", class_="main-article")
links = article.find_all("a", href=True)

for link in links:
    web = f"{root}/{link['href']}"
    res = requests.get(web)
    content = res.text
    soup = BeautifulSoup(content, "html.parser")

    article = soup.find("article", class_="main-article")
    title = article.find("h1").get_text()
    transcript = article.find("div", class_="full-script").get_text(strip=True, separator=" ")

    with open(f"{title}.txt", "w", encoding="utf-8") as file:
        if file.write(transcript):
            print(f"scraping... {title}")
