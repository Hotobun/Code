from sqlalchemy import Column,Integer,String, DateTime, func
from config import DB_URI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

engine = create_engine(DB_URI,echo=True)
Session = sessionmaker(bind=engine)
session = Session()
# 所有的类都要继承自`declarative_base`这个函数生成的基类
Base = declarative_base(engine)
class Replies(Base):
    # 定义表名
    __tablename__ = 'replies'

    # 将id设置为主键，并且默认是自增长的
    # Column常用参数:
    # default：默认值。
    # nullable：是否可空。
    # primary_key：是否为主键。
    # unique：是否唯一。
    # autoincrement：是否自动增长。
    # onupdate：更新的时候执行的函数。
    # name：该属性在数据库中的字段映射。
    mid = Column(Integer,)
    oid = Column(Integer,name = "AV")
    rpid = Column(String(20),primary_key = True, unique=True)
    rcount = Column(Integer,name = "回复量")
    ctime = Column(DateTime,name= "time")
    like = Column(Integer,name="点赞")
    root = Column(String(20))
    uname = Column(String(20))
    sex = Column(String(4),)
    sign = Column(String(200))
    level = Column(Integer,)
    message = Column(String(2222))
    
    def __repr__(self):
        return '<Replies(rpid="{}", message="{}...")>'.format(self.rpid, self.message[:20])

def insert(item):
    # item type : dict
    # 插入数据
    if type(item) == dict:
        new = Replies()
        new.mid = item["mid"]
        new.oid = item["oid"]
        new.rpid = str(item["rpid"])
        new.rcount = item["rcount"]
        # 时间截转为datetime对象 # datetime.datetime.fromtimestamp(ctime)
        new.ctime = datetime.datetime.fromtimestamp(item["ctime"])
        new.like = item["like"]
        new.root = str(item["root"])
        new.uname = item["member"]["uname"]
        new.sex = item["member"]["sex"]
        new.sign = item["member"]["sign"]
        new.level = item["member"]["level_info"]["current_level"]
        new.message = init_str(item["content"]["message"])

        # 查找id是否在数据表里已存在
        temp = session.query(Replies).filter_by(rpid=item['rpid']).all()
        if temp:
            temp = new 
        else:
            session.add(new)
        print("item --> ", new)
        session.commit()

def init_str(str):
    # 有的热心市民拿QQ的默认表情到B站回复
    # 居然还能加载 编码是12w+ 这里把十万以上的编码字符全都过滤了 不然会乱码报错
    for i in str:
        if ord(i) > 100000:
            str = str.replace(i, '')
    return str

def Create_table():
    # 创建数据表
    Base.metadata.create_all()
    print("table {} 创建成功".format(Replies.__tablename__))

if __name__ == "__main__":
    Create_table()