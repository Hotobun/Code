HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'bilibili'
USERNAME = 'root'
PASSWORD = '密码'
# mysql数据库URI
# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

# 查看爬取状态 关了什么都看不到
debug = True

# 每页爬取间隔 太少容易失败 单位秒
timeout = 0.9

# 番剧页面 这里的page=1 换成了 page={} 便于后面替换 能用就不需要改
animeurl = 'https://api.bilibili.com/pgc/season/index/result?season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&page=1&season_type=1&pagesize=20&type=1'

# 浏览器f12 headers里面内容直接复制过来 下面那个head会转成能用的dict 
htmlheaders = '''一对三单引号里面'''

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