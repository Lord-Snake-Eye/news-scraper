from bs4 import BeautifulSoup
import requests
import yagmail
import dotenv
import os
import time
dotenv.load_dotenv()


class News:

    news = []
    sources = []
    body = ''

    def __init__(self, category):
        self.url = f'https://myrepublica.nagariknetwork.com/category/{category}'
        self.category = category
        self.res = requests.get(self.url).content
        self.soup = BeautifulSoup(self.res, 'html.parser')
        self.appendNews()

    def appendNews(self):
        print("Collecting News.....")
        mainHeading = self.soup.select(
            '.categories-list-info .main-heading')

        for i in mainHeading:
            headline_text = i.find('h2').text
            source_link = [a['href'] for a in i.find_all('a', href=True)]
            source = f"https://myrepublica.nagariknetwork.com{source_link[0]}"
            self.news.append(headline_text)
            self.sources.append(source)

        for index, content in enumerate(self.news):
            self.body += f"{index+1}. {content}\nSource: {self.sources[index]}\n\n"
        print("Collecting News Completed.....")

    def displayNews(self):
        return self.body

    def send_mail(self, reciever=[]):
        print("Sending Email...")
        self.reciever = reciever
        yag = yagmail.SMTP(os.getenv('EMAIL'), os.getenv('PASSWORD'))
        yag.send(
            to=self.reciever,
            subject=f"Daily News Headlines - {self.category.capitalize()}",
            contents=self.body
        )
        print("Finished sending emails.")
