
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import request

chrome_path = r"C:\Selenium\chromedriver.exe"


def vid_load(my_url, vid_name, class_of_link):

    #driver = webdriver.Chrome(chrome_path)
    #url = r"http://myshoutbox.tk/signup.php"
    #driver.get(url)   
    new_url = r'http://downsub.com/?url='
    my_url = my_url.replace('/', '%2F')
    my_url = my_url.replace(':', '%3A')
    my_url = my_url.replace('?', '%3F')
    my_url = my_url.replace('=', '%3D')
    new_url += my_url
    print(new_url)

    resp = request.urlopen(new_url).read()
    soup = BeautifulSoup(resp, "html.parser")

    down_anchor = soup.find_all('a')
    down_link = r'http://downsub.com'
    for each in down_anchor:
        if down_anchor['href'] != '':
            link = down_anchor['href']
            down_link += link[1:]
            break
    print(down_link)

    driver = webdriver.Chrome(chrome_path)
    driver.get(down_link)
    driver.quit()

vid_load(r'https://www.youtube.com/watch?v=l-KQYWzDU1A', 'Hello', "btn btn-outline btn-sm")

#<a href="javascript:;" onclick="downloadConfirm(event,'video')" class="btn btn-outline btn-sm curr">Download Pro</a>
#<a href="https://r6---sn-n4v7sn7y.googlevideo.com/videoplayback?sparams=dur%2Cei%2Cid%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cexpire&amp;requiressl=yes&amp;ei=A1k0Wa-7EfyE1wK0mKjwAw&amp;mt=1496602772&amp;mm=31&amp;ip=159.253.144.86&amp;lmt=1473446863624607&amp;mn=sn-n4v7sn7y&amp;ratebypass=yes&amp;itag=22&amp;key=yt6&amp;source=youtube&amp;mv=m&amp;ipbits=0&amp;ms=au&amp;signature=D15DA0C10CECAF7F0FFA06AF1016F70DA76966B8.361356F93E286C120C21B3676676B2B50E1BE57E&amp;expire=1496624483&amp;dur=536.427&amp;id=o-AOSp3-6IrGkXSH6QnqfmmYAnhxvj79md7QcJCu0qRfLd&amp;pl=24&amp;mime=video%2Fmp4&amp;title=Voy+A+La+Escuela+%28I%27m+Going+to+School%29+Bilingual+Book+READ+ALOUD" download="Voy A La Escuela (I'm Going to School) Bilingual Book READ ALOUD (Max 720p).mp4" class="btn btn-outline btn-sm" onclick="openPopUp();">Download</a>
#<a href="./index.php?title=Voy+A+La+Escuela+%28I%27m+Going+to+School%29+Bilingual+Book+READ+ALOUD&amp;url=https%3A%2F%2Fwww.youtube.com%2Fapi%2Ftimedtext%3Fhl%3Den_US%26caps%3Dasr%26expire%3D1496627356%26sparams%3Dasr_langs%252Ccaps%252Cv%252Cexpire%26v%3Dl-KQYWzDU1A%26asr_langs%3Dpt%252Cnl%252Cru%252Ces%252Cfr%252Cja%252Cen%252Cit%252Cko%252Cde%26key%3Dyttt1%26signature%3D0D5725709FFEC4D9CD2ECBBEAE68BA99CA932D02.096A35AD34BA5F25A0C56313960539D19EA54BB2%26kind%3Dasr%26lang%3Den">&gt;&gt;Download&lt;&lt;</a>
