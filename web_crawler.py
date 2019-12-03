import json
import time
import mysql.connector
from mysql.connector import Error
import multiprocessing as mp

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

#MySQL Server parameters
host = 'localhost'
password = ''
Database_Name = 'crawler'
username = 'root'

def store_data(sqldatabase,data,result_id):
    fields = ['id', 'download', 'upload', 'latency', 'date', 'distance', 'country_code', 'server_id',
              'server_name',
              'sponsor_name', 'sponsor_url', 'connection_mode', 'isp_name', 'isp_rating', 'test_rank',
              'test_grade',
              'test_rating', 'path']
    strfields = ['country_code','server_name','sponsor_name','sponsor_url','connection_mode','isp_name',
                 'test_grade','path']
    print("Result ID " +str(result_id)+ " Data fetched. Now storing.")
    for k in fields:
        if k not in data.keys():
            if k in strfields:
                data[k] = 'NA'
            else:
                data[k] = -1
    #Escaping sponsor_name so it can be inserted without error into the database
    for j in strfields:
        temp = str(data[j])
        temp = list(temp)
        for i in range(len(temp)):
            if temp[i] == "'":
                temp[i] = "''"
        data[j] = ''.join(temp) 
    #Adding values to table
        cursor = sqldatabase.cursor()
        #Query to Insert values
        command_string =f'''INSERT INTO {Table_Name} VALUES(
            {int(data['id'])},
            {int(data['download'])},
            {int(data['upload'])},
            {int(data['latency'])},
            {int(data['date'])},
            {int(data['distance'])},
            '{str(data['country_code'])}',
            {int(data['server_id'])},
            '{str(data['server_name'])}',
            '{str(data['sponsor_name'])}',
            '{str(data['sponsor_url'])}',
            '{str(data['connection_mode'])}',
            '{str(data['isp_name'])}',
            {float(data['isp_rating'])},
            {int(data['test_rank'])},
            '{str(data['test_grade'])}',
            {float(data['test_rating'])},
            '{str(data['path'])}'
            );'''
        cursor.execute(command_string)
        sqldatabase.commit()
        print("Data stored")
        cursor.close()
        sqldatabase.close()

def fetch_data(result_id):
    #This part of the function fetches the data only if data is not already in the table
    try:
        sqldatabase = mysql.connector.connect(host = host,user = username,database=Database_Name,password = password)
    except Error as e:
        print ('Error encountered while conencting to SQL server to check if entry exists:- ',e)
        return
    else:
        if sqldatabase.is_connected():
            cursor = sqldatabase.cursor()
            cursor.execute(f"SELECT * FROM {Table_Name} WHERE path LIKE 'result/{result_id}'")
            if not cursor.fetchone():
                #If entry not in table, data is fetched
                cursor.close()     
                url = f"https://www.speedtest.net/result/{result_id}"
                ua = UserAgent(verify_ssl = False)
                header = {'User-Agent': str(ua.chrome)}
                url_data = requests.get(url, headers=header)

                while url_data.status_code == 429:
                    print("Hit", end=" ")
                    time.sleep(20)
                    url_data = requests.get(url)

                if url_data.status_code == 404:
                    print("404 Error Code")
                    return

                elif url_data.status_code == 200:
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
                    #Function Call to store data in database
                    if data:
                        store_data(sqldatabase,data,result_id)
                        sqldatabase.close()
            else:
                #If entry is in table
                print ('Result ID',result_id,'Already in Database')
                cursor.close()
                sqldatabase.close()
                return

def create_table(ID):
    try:
        sqldatabase = mysql.connector.connect(host = host,user = username,database=Database_Name,password = password)
    except Error as e:
        print ('Error encountered while conencting to SQL server :- ',e)
        exit()
    else:
        if sqldatabase.is_connected():
                #Creating table
                cursor = sqldatabase.cursor()
                global Table_Name
                Table_Name = f'result_data_{ID}'
                cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {Table_Name} (
                id int(20),
                download int,
                upload int,
                latency int,
                date int(20),
                distance int,
                country_code varchar(4),
                server_id int(20),
                server_name varchar(200),
                sponsor_name varchar(200),
                sponsor_url varchar(200),
                connection_mode varchar(50),
                isp_name varchar(200),
                isp_rating float(4),
                test_rank int,
                test_grade varchar(3),
                test_rating float(4),
                path varchar(50)
                );
                ''')
                cursor.close()
                sqldatabase.close()

def crawler(ID, steps):
    create_table(ID)
    #Pooling URL's
    pool = mp.Pool(mp.cpu_count())
    pool.imap_unordered(fetch_data,[(ID + i) for i in range(steps)])
    pool.close()
    pool.join()
    
