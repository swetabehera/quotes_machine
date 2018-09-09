import requests
from bs4 import BeautifulSoup
from random import choice
import csv
from csv import writer
article_all=list()
for x in range(1,11):
	response = requests.get("http://quotes.toscrape.com/page/"+str(x)+"/")
	soup= BeautifulSoup(response.text,"html.parser")
	articles=soup.find_all(class_="quote")
	article_all.extend(articles)

article=choice(article_all)
quote=article.find(class_="text").get_text()
author=article.find(class_="author").get_text()
url=article.find("a")['href']
re=requests.get("http://quotes.toscrape.com"+url)
so=BeautifulSoup(re.text,"html.parser")
first_letter=author[0]
last_letter=author.split()[-1][0]
born=so.find(class_="author-born-date").get_text()+" "+so.find(class_="author-born-location").get_text()
print(quote,author,born,first_letter,last_letter)

#with open("web_scr.csv","w") as file:
#	csv_writer=writer(file)
#	csv_writer.writerow(["Name","URL","Time"])
#	for article in articles:
#		title=article.find("a").get_text()
#		url=article.find("a")['href']
#		time=article.find("time")["datetime"]
#		csv_writer.writerow([title,url,time])

