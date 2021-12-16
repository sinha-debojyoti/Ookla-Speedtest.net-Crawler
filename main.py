import time
import web_crawler


if __name__ == '__main__':
    #Starting URL
    ID = 1000000000

    # Number of URLS data to be fetched
    steps = 10

    start = time.time()
    web_crawler.crawler.remote(ID,steps)
    print("--- %s seconds taken for %s records ---" % ((time.time() - start),steps))
