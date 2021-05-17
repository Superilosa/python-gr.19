import requests
import json
from bs4 import BeautifulSoup, Tag
from urllib.parse import urljoin

#1
URL = "https://dataquestio.github.io/web-scraping-pages/ids_and_classes.html"
response = requests.get(URL)
if 200 <= response.status_code < 300:
    print("Request successful", response.status_code)
    html = BeautifulSoup(response.content, "html.parser")
    for element in html.find_all(id="first"):
        print(element.text)
else:
    print("Request unsuccessful", response.status_code)

#2
URL = "https://btu.edu.ge/ka/contact"
response = requests.get(URL)
if 200 <= response.status_code < 300:
    print("Request successful", response.status_code)
    html = BeautifulSoup(response.content, "html.parser")
    info_html = html.find(attrs={"class" : "contact_infos"})

    address_content = info_html.find(attrs={"class" : "contact_address"}).text.strip()
    phone_content = info_html.find(attrs={"class" : "contact_telephone"}).text.strip()
    #იმეილი წერია javascript კოდით და სწორი ტექსტი არ ამოდის
    email_content = info_html.find(attrs={"class" : "contact_email_to"}).text.strip()
    transport_content = info_html.find(attrs={"class" : "contact_moreinformation"}).text.strip()

    address = address_content.split(':')
    phone = phone_content.split(':')
    email = email_content.split(':')
    transport = transport_content.split(':')
    transport = transport[1].split('მიკროავტობუსით')
    bus = transport[0].replace('ავტობუსით', '').replace('ან', '').replace('\n', '').replace('\r', '').strip().split(',')
    minibus = transport[1].strip().split(',')

    dict = {address[0] : address[1].strip(), phone[0] : phone[1].strip(), email[0] : email[1].strip(), "ავტობუსის ნომრები" : bus, "მიკროავტობუსის ნომრები" : minibus}

    with open('info.json', 'w') as file:
        json.dump(dict, file, indent=4)

else:
    print("Request unsuccessful", response.status_code)

#3
URL = "http://quotes.toscrape.com/"


class Author:
    def __init__(self, name, born, description):
        self.name = name
        self.born = born
        self.description = description

    def __eq__(self, item):
        return item == self.name

    def __str__(self):
        return self.name

    def dictionary(self):
        dict = {"Name" : self.name, "Born" : self.born, "Description" : self.description}
        return dict


authors = []


def about_author(about_url):
    response = requests.get(about_url)
    if 200 <= response.status_code < 300:
        print("Request successful", response.status_code)
        html = BeautifulSoup(response.content, "html.parser")
        html_about = html.find(attrs={"class": "author-title"})
        about_text = html_about.text.split('\n')
        name = about_text[0]
        born = about_text[1].split(':')[1].strip()
        description = about_text[4].strip()
        author = Author(name, born, description)
        authors.append(author)

    else:
        print("Request unsuccessful", response.status_code)


def find_author(url):
    response = requests.get(url)
    if 200 <= response.status_code < 300:
        print("Page load successful", response.status_code)
        html = BeautifulSoup(response.content, "html.parser")
        for html_author_name in html.find_all(attrs={"class" : "author"}):
            already_added = False
            for author in authors:
                if html_author_name.text == author:
                    already_added = True
            if already_added:
                continue
            html_author = html_author_name.parent
            about_link = html_author.a['href']
            about_link = urljoin(URL, about_link)
            about_author(about_link)
        html_next_page = html.find("li", attrs={"class" : "next"})
        if html_next_page:
            next_page = html_next_page.a['href']
            next_page = urljoin(URL, next_page)
            find_author(next_page)

    else:
        print("Error loading page", response.status_code)


find_author(URL)
with open('about_authors.json', 'w') as file:
    for author in authors:
        json.dump(author.dictionary(), file, indent=4)
        file.write('\n')