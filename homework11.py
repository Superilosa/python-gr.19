import requests
from bs4 import BeautifulSoup
import sqlite3
from urllib.parse import urljoin


#1
URL1 = "https://ka.wikipedia.org/wiki/24_%E1%83%9B%E1%83%90%E1%83%98%E1%83%A1%E1%83%98"
URL2 = "https://ka.wikipedia.org/wiki/25_%E1%83%9B%E1%83%90%E1%83%98%E1%83%A1%E1%83%98"
URL3 = "https://ka.wikipedia.org/wiki/26_%E1%83%9B%E1%83%90%E1%83%98%E1%83%A1%E1%83%98"


def day_info(url, connection, cursor, holidays_delimiter):
    response = requests.get(url)
    if 200 <= response.status_code < 300:
        print("ვებსაიტთან წვდომა წარმატებით განხორციელდა", response.status_code)
        html = BeautifulSoup(response.content, "html.parser")
        info_html = html.find("div", attrs={"class" : "mw-parser-output"})
        for subtitle in info_html.findChildren("ul", recursive=False):
            title = subtitle.find_previous_sibling("h2").find("span", attrs={"class" : "mw-headline"}).get('id')
            if title == 'დღის_მოვლენები':
                table = "events"
                delimiter = (':')
            elif title == 'ამ_დღეს_დაბადებულნი':
                table = "births"
                delimiter = (':')
            elif title == 'ამ_დღეს_გარდაცვლილნი':
                table = "deaths"
                delimiter = (':')
            elif title == 'მსოფლიოს_ქვეყნების_დღესასწაულები':
                table = "holidays"
                delimiter = holidays_delimiter
            else:
                continue
            for event_content in subtitle.findChildren("li", recursive=False):
                event = event_content.text.split(delimiter)
                if len(event) == 1:
                    if len(event[0]) < 5:
                        value1 = event[0].replace('\xa0', '')
                        value2 = None
                    else:
                        value2 = event[0].replace('\xa0', '')
                        value1 = None
                else:
                    value1 = event[0].replace('\xa0', '')
                    value2 = event[1].replace('\xa0', '')
                cursor.execute(f"INSERT INTO {table} VALUES ('{value1}', '{value2}')")
                connection.commit()

    else:
        print("ვებსაიტთან წვდომა ვერ მოხერხდა", response.status_code)


def create_database():
    connection = sqlite3.connect('homework11.db')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS events (Year INTEGER, Event TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS births (Year INTEGER, Person TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS deaths (Year INTEGER, Person TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS holidays (Countries TEXT, Holiday TEXT)")
    connection.commit()
    return connection, cursor


# connection, cursor = create_database()
# day_info(URL1, connection, cursor, '-')
# day_info(URL2, connection, cursor, ',')
# day_info(URL3, connection, cursor, '-')



#2
url_base = "http://www.heraldika.ge/"
URL = "http://www.heraldika.ge/index.php?m=41&p_news=1"


def find_heraldry(url):
    response = requests.get(url)
    if 200 <= response.status_code < 300:
        print("ვებსაიტთან წვდომა წარმატებით განხორციელდა", response.status_code)
        html = BeautifulSoup(response.content, "html.parser")
        for arms in html.find_all("div", attrs={"class" : "arms_img"}):
            info_link = arms.find('a').get('href')
            info_url = urljoin(url_base, info_link)
            get_heraldry(info_url)
        next_page = html.find("img", attrs={"src" : "images/next.png"}).parent.parent
        if next_page.name == 'a':
            next_page_link = next_page.get("href")
            next_page_url = urljoin(url_base, next_page_link)
            find_heraldry(next_page_url)

    else:
        print("ვებსაიტთან წვდომა ვერ მოხერხდა", response.status_code)


def get_heraldry(url):
    response = requests.get(url)
    if 200 <= response.status_code < 300:
        print("ლინკზე გადასვლა წარმატებით განხორციელდა", response.status_code)
        html = BeautifulSoup(response.content, "html.parser")
        municipality = html.head.find("meta", attrs={"property" : "og:title"}).get("content")
        html_content = html.find("div", attrs={"class" : "armstxt"})
        coat = True
        for image_tag in html_content.find_all("td"):
            for image in image_tag.find_all("img"):
                image_link = image.get('src')
                image_url = urljoin(url_base, image_link)
                download_heraldry(image_url, municipality, coat)
                coat = False

    else:
        print("ლინკზე გადასვლა ვერ მოხერხდა", response.status_code)


def download_heraldry(url, municipality, coat):
    response = requests.get(url)
    if 200 <= response.status_code < 300:
        print("ფოტოზე გადასვლა წარმატებით განხორციელდა", response.status_code)
        if coat:
            file_name = municipality + "_გერბი"
        else:
            file_name = municipality + "_დროშა"
        with open(f"Heraldry/{file_name}.jpg", 'bw') as file:
            file.write(response.content)


    else:
        print("ფოტოზე გადასვლა ვერ მოხერხდა", response.status_code)

find_heraldry(URL)