import os, time, requests, pickle, json
import replies_db
import time
from config import replyrooturl, replyurl, headers, timeout, oid

def append_replies(orpage, oid,root):
    # orpage type : int # 番剧评论第几页
    # oid type : int    # 番剧AV号
    # root type : int   # 评论的根
    # page type ： int  # 回复根评论的第几页
    page = 0
    while True:
        page += 1
        url = replyurl.format(page=page, oid=oid,root=root,pageadd1= page+1)
        dirpath = os.path.join("AV{}".format(oid),str(orpage))
        savename = "page{}_{}_{}.json".format(orpage,root,page) # str(orpage)+"_{}_{}".format(root,page)
        data = get_jsonlist(url, dirpath, savename)
        if not data:
            print("AV{}第{}页 root{}已无数据".format(oid,orpage,page))
            return 
        for item in data:
            if "rpid" in item:
                replies_db.insert(item)

def get_jsonlist(url,dirpath, savename):
    # all argc type : str
    # rtype : list
    txt = ''
    sleep = False
    filename = os.path.join(dirpath, savename)
    if os.path.isfile(filename):
        with open(filename, 'r', encoding = "utf-8") as f:
            txt = f.read()
    else:
        r = requests.get(url, headers = headers )
        sleep = True
        print("url --> ", url)
        txt = r.text[r.text.index("(")+1:r.text.rindex(")")]
        save(txt,dirpath,savename)
    try:
        data = json.loads(txt)
    except:
        data = dict()
    if "data" in data:
        if "replies" in data["data"]:
            if sleep:
                time.sleep(timeout)
            return data["data"]["replies"]
    return []

def main():
    page = 0
    while True:
        page += 1
        url = replyrooturl.format(page=page, oid = oid)
        data = get_jsonlist(url,dirpath = os.path.join("AV{}".format(oid),str(page)), savename = "page{}.json".format(page))
        if not data:
            print("AV{}第{}页已无数据".format(oid,page))
            break
        for item in data:
            # 追评默认显示3个 已经在上面的response  
            # 如果超过三个 就要再访问api获取
            if "rpid" in item:
                replies_db.insert(item)
                if item['rcount'] == 0:
                    continue
                if item['rcount'] <= 3:
                    for i in item["replies"]:
                        if "rpid" in i:
                            replies_db.insert(i)
                else:
                    append_replies(orpage=page,oid = oid, root = item["rpid"])

def save(txt, dirpath, filename):
    if not os.path.isdir(dirpath):
        if not os.path.isdir("AV{}".format(oid)):
            os.mkdir("AV{}".format(oid))
        os.mkdir(dirpath)
    with open(os.path.join(dirpath,filename),"w", encoding = "utf-8") as f:
            f.write(txt)

if __name__ == "__main__":
    main()
