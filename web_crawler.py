import json
import time
import multiprocessing as mp

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from database import Database

def fetch_data(result_id):
    url = f"https://www.speedtest.net/result/{result_id}"

    ua = UserAgent()
    header = {'User-Agent': str(ua.chrome)}

    url_data = requests.get(url, headers=header)

    if url_data.status_code == 404:
        return

    while url_data.status_code == 429:
        print("Hit", end=" ")
        time.sleep(20)
        url_data = requests.get(url)

    if url_data.status_code == 200:
        soup = BeautifulSoup(url_data.content, 'html5lib')

        script_data = ""
        try:
            script_data = soup.find_all("script")[6]
        except:
            print("404 Error Code")
            return

        script_data_to_text = script_data.get_text()

        start = script_data_to_text.find("window.OOKLA.INIT_DATA=")
        end = script_data_to_text.find(",window.OOKLA.globals=")

        init_data = script_data_to_text[start:end]

        start = init_data.find("""{"id""")
        final_data = init_data[start:-1]

        data = json.loads(final_data)

        del url, url_data, soup, script_data, script_data_to_text, init_data, final_data, start, end

        TOTAL_BIT=1024 # For Converting SPeed into MB.
        data['isp_rating'] = float(data['isp_rating'])
        data['id'] = int(data['id'])
        data['download']=round(data['download']/TOTAL_BIT+0.01,2)
        data['upload']=round(data['upload']/TOTAL_BIT+0.01,2)

        fields = {'id':'int(11)','download':'decimal(18,2)','upload':'decimal(18,2)',
              'latency':'int(5)','date':'int(11)','distance':'int(5)',
              'country_code':'varchar(3)','server_id':'int(5)',
              'server_name':'varchar(25)','sponsor_name':'varchar(30)'
              ,'sponsor_url':'varchar(6)','connection_mode':'varchar(10)',
              'isp_name':'varchar(25)','isp_rating':'float','test_rank':'int(5)',
              'test_grade':'varchar(5)','test_rating':'float','path':'varchar(30)'}
 

        connection = Database(table_name='crawler',fields=fields)
        connection.insert(data)
        
def crawler(ID=1000000000, steps=2):
    pool = mp.Pool(mp.cpu_count()) 
    pool.imap_unordered(fetch_data,[ID+i for i in range(steps)])
    pool.close()
    pool.join()
