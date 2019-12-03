import web_crawler
import time

start = time.time()
ID = 1000000000
steps = 10

web_crawler.crawler(ID, steps)
print("--- %s seconds taken for %s records ---" % ((time.time() - start),steps))
