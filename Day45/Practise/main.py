from bs4 import BeautifulSoup
import requests
#
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# #
# # print(soup.h1)
# # print(soup.title.name)
# # print(soup.title)
# # print(soup.title.string)
# #
# # print(soup.prettify())
#
# # print(soup.p)
#
# all_anchor_gags = soup.find_all(name="a")
# # print(all_anchor_gags)
# #
# # for tag in all_anchor_gags:
# #     # print(tag.getText())
# #     tag.get("href")
#
# # heading = soup.find(name="h1", id="name")
# # print(heading)
#
# # sec_heading = soup.find(name="h3", class_="heading")
# # print(sec_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a")

articles_text = []
articles_links = []
articles_upvote = []

for article_tag in articles :
    article_text = article_tag
    articles_text.append(article_text)
    article_link = article_tag.get("href")
    articles_links.append(article_link)


articles_upvote = [score.getText for score in soup.find_all(name="span", class_="score")]


# print(articles_text)
# print(articles_links)
print(articles_upvote[0])
