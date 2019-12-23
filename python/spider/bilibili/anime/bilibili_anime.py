from lxml import etree
import os, time, requests, pickle, json
import bilibili_db
import time
from config import animeurl, headers, debug, timeout

def main():
    for page in range(1,152):  # max_page = 151
        r = requests.get(animeurl.replace("page=1", "page={}".format(page)), headers = headers )
        with open("pkl/page{}.pkl".format(page), 'wb') as f:
            pickle.dump(r, f)
        data = json.loads(r.text)["data"]["list"]
        bilibili_db.insert(data)
        if debug:
            print(r.url, "done")
        time.sleep(timeout)

if __name__ == "__main__":
    main()
