from bs4 import BeautifulSoup
from urllib import request


def des_load(my_url, *id_kargs):
    try:
        #proxies = {'http': 'http://www.someproxy.com:3128'}
        #filehandle = urllib.urlopen(some_url, proxies=proxies)
        #urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
        resp = request.urlopen(my_url).read()
        soup = BeautifulSoup(resp, "html.parser")
        #print(soup.prettify())
        #for link in soup.find_all('a'):
        #    print(link.get_text(), link.get('href'))
        publish_date = soup.find(id = id_kargs[0]).get_text()
        description = soup.find(id = id_kargs[1])

        
        video_title = soup.find(id = id_kargs[2]).get_text()
        video_words = video_title.split()
        vid = ''
        for each in video_words:
            each.strip()
            vid += each
            vid += '_'
        vid += '.txt'

        
        rest_data = soup.find_all('ul', {'class': id_kargs[3]})

        
        category = ''
        license_data = ''


        print(vid)
        f = open(vid, 'w')
        print(publish_date)
        f.write(publish_date)
        f.write('\n')


        for each in description:
            try:
                try:
                    f.write(each['href'])
                    print(each['href'], end = '')
                except:
                    pass
                text = each.get_text()
                if text != '':
                    f.write(' { ' + text + ' } ')
                    print(' { ' + text + ' } ')
            except:
                f.write('\n')
                f.write(each)
                f.write('\n')
                print(each)
        counter = 0
        for each in rest_data:
            if counter == 0:
                category = each.get_text()
            else:
                license_data = each.get_text()
            counter += 1
        
        
        print(category.strip())
        print(license_data.strip())
        f.write('Category: ' + category.strip())
        f.write('\n')
        f.write('License: ' + license_data.strip())
        f.write('\n')
        f.close()
    except Exception as e:
        print(str(e))
        
des_load(r'https://www.youtube.com/watch?v=du7lkPPIPbo',  'watch-uploader-info', 'eow-description', 'eow-title', 'content watch-info-tag-list')


#https://r1---sn-n4v7sn7y.googlevideo.com/videoplayback?dur=361.813&requiressl=yes&expire=1496622103&id=o-APH5Oc6v_TgmSJxOo-zLA-4wZwIDinNu7_0-RxwZfHWx&key=yt6&mn=sn-n4v7sn7y&mm=31&signature=2E8EAC3A2FEC88FA612C870334275272BD0C5D62.160A09F1FF05C830DC2CE4D4C2C130FC3580E1C1&ip=159.253.144.86&ratebypass=yes&mv=m&lmt=1496554928227541&sparams=dur%2Cei%2Cid%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cexpire&source=youtube&ms=au&mime=video%2Fmp4&ei=t080WbPtJIGG1wKXoo6ICw&mt=1496600377&pl=24&itag=22&ipbits=0&title=Yu+Yureka+Black+-+Yu+Nailed+it%21%21%21+Another+Copy%3F
