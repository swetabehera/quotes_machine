import requests
from bs4 import BeautifulSoup
from random import choice
import csv
from time import sleep
from csv import writer
article_all=list()
for x in range(1,11):
	response = requests.get("http://quotes.toscrape.com/page/"+str(x)+"/")
	soup= BeautifulSoup(response.text,"html.parser")
	articles=soup.find_all(class_="quote")
	article_all.extend(articles)
	sleep(3)



sweta=True
while(sweta):
	article=choice(article_all)
	quote=article.find(class_="text").get_text()
	author=article.find(class_="author").get_text()
	url=article.find("a")['href']
	re=requests.get("http://quotes.toscrape.com"+url)
	so=BeautifulSoup(re.text,"html.parser")
	first_letter=author[0]
	last_letter=author.split()[-1][0]
	born=so.find(class_="author-born-date").get_text()+" "+so.find(class_="author-born-location").get_text()
	
	print("Here's a quote:\n")
	print(quote)
	x=4
	answer=input("\nWho said this? Guesses remaining "+str(x)+"\n")
	if answer ==  author:
		print("You guessed correctly! Congratulations !!!")
		article_all.remove(article)
	else:
		x=x-1
		print("Here's a hint. The author was born on "+ born)
		answer=input("\nWho said this? Guesses remaining "+str(x)+"\n")
		if answer ==author:
			print("You guessed correctly! Congratulations !!!")
			article_all.remove(article)
		else:
			x=x-1
			print("Here's a hint. The author's first name starts with "+ first_letter)
			answer=input("\nWho said this? Guesses remaining "+str(x)+"\n")
			if answer ==author:
				print("You guessed correctly! Congratulations !!!")
				article_all.remove(article)
			else:
				x=x-1
				print("Here's a hint. The author's last name starts with "+ last_letter)
				answer=input("\nWho said this? Guesses remaining "+str(x)+"\n")
				if answer ==author:
					print("You guessed correctly! Congratulations !!!")
					article_all.remove(article)
				else: 
					print("Sorry, You have run out of Guesses. The answer is "+author)
					article_all.remove(article)
	ch=input("Would you like to play again?(y/n)\n")
	if ch=="n":
		sweta=False


# with open("web_scr2.csv","w") as file:
# 	csv_writer=writer(file)
# 	csv_writer.writerow(["Quote","Author","Birth","First Name Initial","Last Name Initial"])
# 	for article in article_all:
# 		quote=article.find(class_="text").get_text()
# 		author=article.find(class_="author").get_text()
# 		url=article.find("a")['href']
# 		re=requests.get("http://quotes.toscrape.com"+url)
# 		so=BeautifulSoup(re.text,"html.parser")
# 		first_letter=author[0]
# 		last_letter=author.split()[-1][0]
# 		born=so.find(class_="author-born-date").get_text()+" "+so.find(class_="author-born-location").get_text()
# 		csv_writer.writerow([quote,author,born,first_letter,last_letter])

