import time
import web_crawler


if __name__ == '__main__':
    ID = 1000000000
    steps = 10
    start = time.time()
    web_crawler.crawler(ID,steps)
    print("--- %s seconds taken for %s records ---" % ((time.time() - start),steps))
