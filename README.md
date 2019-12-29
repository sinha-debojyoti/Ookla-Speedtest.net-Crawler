# Ookla Speedtest.net Crawler
[Join Communication Chanel for Help and Discussion](https://join.slack.com/t/ooklawebcrawler/shared_invite/enQtODQzMDg5MDEwNDE5LTdlZGNiMzg1MDljMDYwMjkyMWFhOTRmYWExNGZjMGI0NWU2MDc4NmU5N2YyY2IyMDk3OTdjYTk5ZWI0ZDU2MGE)

## About
### Ookla Speedtest.net Crawler
A python web crawler that crawls nearly 25 billion pages of https://www.speedtest.net to fetch download speed, upload speed, latency, date, distance, country code, server ID, server name, sponsor name, sponsor URL, connection_mode, isp name, isp rating, test rank, test grade, test rating and path of different surveys and stores them in a mysql database.

## Installation
Download or clone the repository and set up a virtual environment.
```
git clone https://github.com/sinha-debojyoti/Ookla-Speedtest.net-Crawler
cd Ookla-Speedtest.net-Crawler
python3 -m venv venv 
source venv/bin/activate
```
Installing required packages
```
pip install -r requirements.txt
```
Run **main.py** 
```
python3 main.py
```

## Database documentation
MySQL database is used to store the result parsed by the main program.Interaction with the database could be done as follows.

#### Creating a table.
If the table is present already a connection to the same table is provided else new table is made.
```
from database import Database

table_name = 'student'
fields = {'roll_no':'int(5)','first_name:':'varchar(15)','last_name':'varchar(15)'}

connection = Database(table_name='student',fields=fields,filename='config.ini',section='mysql')
```
The configuration of the database is taken from an external configuration file.
##### Format of configuration file(config.ini)
```
[mysql]
host = localhost
database = crawler
user = bob
password = bob
```

#### Inserting data into the table
The data to be inserted is in the form of dictionary with key as the field name and value as the value of the field.
```
data = {'roll_no':12,'first_name':'Rajesh','last_name':'Ingle'}
connection.insert(data)
```

## Modules
```
lxml:Used for parsing page content.
fake_useragent:  Up to date simple useragent faker with real world database
html5lib :pure-python library for parsing HTML
bs4 : for parsing HTML and XML documents
requests :Requests allows you to send organic, grass-fed HTTP/1.1 requests
multiprocessing : Helps for multiprocessing
mysql-connector-python : Enable python programs to access MySQL database
```

## Contributing
follow all [CONTRIBUTING.md](CONTRIBUTING.md) rules.

## Support
19884377+sinha-debojyoti@users.noreply.github.com
