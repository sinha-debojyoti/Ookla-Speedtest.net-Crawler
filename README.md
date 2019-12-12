## Ookla Speedtest.net Crawler
[Join Communication Chanel for Help and Discussion](https://join.slack.com/t/ooklawebcrawler/shared_invite/enQtODQzMDg5MDEwNDE5LTdlZGNiMzg1MDljMDYwMjkyMWFhOTRmYWExNGZjMGI0NWU2MDc4NmU5N2YyY2IyMDk3OTdjYTk5ZWI0ZDU2MGE)

## Table of Contents (Optional)
- [About](#About)
- [Installation](#installation)
- [Modules](#Modules)
- [Contributing](#Contributing)
- [Team](#team)
- [Support](#Support)

## About
### Ookla Speedtest.net Crawler
A python web crawler that fetches nearly 10 billion pages of https://www.speedtest.net to fetch download speed, upload speed, latency, date, distance, country code, server ID, server name, sponsor name, sponsor URL, connection_mode, isp name, isp rating, test rank, test grade, test rating, path and file is stored in form of csv in result_data folder.

## Installation
Visit [Here](https://github.com/sinha-debojyoti/Ookla-Speedtest.net-Crawler) download or create clone on local Directory(in Your System).
```
#If you are using git client use command
>git clone https://github.com/sinha-debojyoti/Ookla-Speedtest.net-Crawler
>cd Ookla-Speedtest.net-Crawler
```
open Command prompt and change Directory to
```
cd Ookla-Speedtest.net-Crawler
```
Install required packages from **requirements.txt**.
```
pip install -r requirements.txt
```
wait until to install packages libraries.

Now its time to execute **main.py** file
```
python main.py
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



##### main.py
```python
import web_crawler

ID = 1000000000 #Starting Result ID
steps = 10 #Number of result at a time

web_crawler.crawler(ID, steps)
```
## Support
19884377+sinha-debojyoti@users.noreply.github.com
