
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import request

chrome_path = r"C:\Selenium\chromedriver.exe"


def vid_load(my_url, vid_name, class_of_link):

    #driver = webdriver.Chrome(chrome_path)
    #driver.get(url)   
    new_url = r'http://keepvid.com/?url='
    my_url = my_url.replace('/', '%2F')
    my_url = my_url.replace(':', '%3A')
    my_url = my_url.replace('?', '%3F')
    my_url = my_url.replace('=', '%3D')
    new_url += my_url

    resp = request.urlopen(new_url).read()
    soup = BeautifulSoup(resp, "html.parser")

    down_anchor = soup.find('a', {'class': class_of_link})
    down_link = down_anchor['href']
    print(down_link)

    driver = webdriver.Chrome(chrome_path)
    driver.get(down_link) 

    #file = open( '1.mp4', 'wb')
    #download = request.urlopen(down_link).read()
    #print(down_link)
    #for line in download:
    #        file.write(line)
    #        file.close()

vid_load(r'https://www.youtube.com/watch?v=ikVHHmaFWck', 'Hello', "btn btn-outline btn-sm")

