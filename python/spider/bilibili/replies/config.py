HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'bilibili'
USERNAME = 'root'
PASSWORD = 'password'
# mysql数据库URI
# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

# 番剧评论的url format需要参数 (page, oid)
replyrooturl = 'https://api.bilibili.com/x/v2/reply?callback=jQuery172044594165909234196_1577181706232&jsonp=jsonp&pn={page}&type=1&oid={oid}&sort=2'
# 回复评论的url format需要参数(page+1,page,oid,root)
replyurl = "https://api.bilibili.com/x/v2/reply/reply?callback=jQuery17205940611368960276_157718824865{pageadd1}&jsonp=jsonp&pn={page}&type=1&oid={oid}&ps=10&root={root}"

# 每页爬取间隔 太少容易失败 单位秒
timeout = 3

# oid 视频AV号
oid = 45316432

# 浏览器f12 headers里面内容直接复制过来 下面那个get_headers会转成能用的dict 
htmlheaders = ''' '''

def get_headers(data = htmlheaders):
    # htmlherders type : str
    # rtype : dict
    # 转换为可使用的字典
    d = dict()
    for i in data.split("\n"):
        if i == "":
            continue
        d[i.split(":")[0]] = i.split(":")[-1]
    return d 

headers = get_headers()
