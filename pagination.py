from bs4 import BeautifulSoup
import requests
count = 0

root = "https://subslikescript.com"
web = f"{root}/movies_letter-A"
print(f"GET {web}")
res = requests.get(web)
content = res.text
soup = BeautifulSoup(content, "html.parser")

# pagination
ul = soup.find("ul", class_="pagination")
li = ul.find_all("li", class_="page-item")
last_page = int(li[-2].text) #133

# for i in range(1, last_page+1): #132+1 # for realworld purposes
for i in range(1, last_page+1)[:1]: # for testing purposes
    res = requests.get(f"{web}?page={i}") #https://subslikescript.com/movies_letter-A?page=1
    soup = BeautifulSoup(res.text, "html.parser")
# /pagination

    # last script
    article = soup.find("article", class_="main-article")
    links = article.find_all("a", href=True)
    for link in links:
        try:
            webs = f"{root}/{link['href']}"
            res = requests.get(webs)
            soup = BeautifulSoup(res.text, "html.parser")

            article = soup.find("article", class_="main-article")
            title = article.find("h1").get_text()
            transcript = article.find("div", class_="full-script").get_text(strip=True, separator=" ")

            with open(f"{title}.txt", "w", encoding="utf-8") as file:
                file.write(transcript)
                count += 1
                print(f"scraping... {title}")
        except:
            print(f"------ LINK NOT FOUND : {link['href']}")

print(f"{count} successfull results")