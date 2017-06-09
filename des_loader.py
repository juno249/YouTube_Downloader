from bs4 import BeautifulSoup
from urllib import request


def des_load(my_url, *id_kargs):
    counter = 0
    while counter < 10:
        counter += 1
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
                        print(each['href'], end = '')
                        f.write(each['href'])
                    except:
                        pass
                    text = each.get_text()
                    if text != '':
                        print(' { ' + text + ' } ')
                        f.write(' { ' + text + ' } ')
                        f.write('\n')
                except:
                    print(each)
                    f.write(each)
                    f.write('\n')
                    
            counter = 0
            for each in rest_data:
                if counter == 0:
                    category = each.get_text()
                else:
                    license_data = each.get_text()
                counter += 1
            
            
            print(category.strip())
            print(license_data.strip())
            f.write('\n\n')
            f.write('Category: ' + category.strip())
            f.write('\n')
            f.write('License: ' + license_data.strip())
            f.write('\n')
            f.close()
            counter = 10
        except Exception as e:
            print(str(e))
            print("Retry: {}".format(counter))
des_load(r'https://www.youtube.com/watch?v=du7lkPPIPbo', 'watch-uploader-info', 'eow-description', 'eow-title', 'content watch-info-tag-list')


