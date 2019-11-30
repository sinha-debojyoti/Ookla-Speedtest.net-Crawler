# Ookla Speedtest.net Crawler
A python web crawler that fetches nearly 10 billion pages of https://www.speedtest.net to fetch download speed, upload speed, latency, date, distance, country code, server ID, server name, sponsor name, sponsor URL, connection_mode, isp name, isp rating, test rank, test grade, test rating, path and file is stored in form of csv in result_data folder.

# Installation
`pip install lxml`
`pip install fake_useragent`
`pip install html5lib`
`pip install bs4`
`pip install requests`

##### main.py
```python
import web_crawler

ID = 1000000000 #Starting Result ID
steps = 10 #Number of result at a time

web_crawler.crawler(ID, steps)
```
# Communication Chanel
https://join.slack.com/t/ooklawebcrawler/shared_invite/enQtODQzMDg5MDEwNDE5LTdlZGNiMzg1MDljMDYwMjkyMWFhOTRmYWExNGZjMGI0NWU2MDc4NmU5N2YyY2IyMDk3OTdjYTk5ZWI0ZDU2MGE
