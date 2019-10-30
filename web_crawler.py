import csv
import json
import time

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def fetch_data(result_id):
    url = "https://www.speedtest.net/result/" + str(result_id)

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

        return data
    else:
        print("404 Error Code")
        return


# ID = 1000000000
# steps = 500

def crawler(ID, steps):
    for i in range(steps):
        data = fetch_data(ID + i)

        if data:
            print("Result ID " + str(ID + i) + " Data fetched,", end=" ")

            fields = ['id', 'download', 'upload', 'latency', 'date', 'distance', 'country_code', 'server_id',
                      'server_name',
                      'sponsor_name', 'sponsor_url', 'connection_mode', 'isp_name', 'isp_rating', 'test_rank',
                      'test_grade',
                      'test_rating', 'path']

            for k in fields:
                if k not in data.keys():
                    data[k] = 'NA'

            # print(data)

            file = 'result_data/' + str(ID) + '.csv'
            with open(file, 'a', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file, lineterminator='\n')

                temp_data = []
                for value in data:
                    temp_data.append(str(data[value]))

                writer.writerow(temp_data)
            csv_file.close()

            print("Data stored")
        else:
            print("404 Error Code")
