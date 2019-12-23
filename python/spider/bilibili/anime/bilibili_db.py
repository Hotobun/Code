from sqlalchemy import Column,Integer,String, DateTime, func
from config import DB_URI, debug
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

engine = create_engine(DB_URI,echo=True)
Session = sessionmaker(bind=engine)
session = Session()
# 所有的类都要继承自`declarative_base`这个函数生成的基类
Base = declarative_base(engine)
class Anime(Base):
    # 定义表名
    __tablename__ = 'anime'

    # 将id设置为主键，并且默认是自增长的
    # Column常用参数:
    # default：默认值。
    # nullable：是否可空。
    # primary_key：是否为主键。
    # unique：是否唯一。
    # autoincrement：是否自动增长。
    # onupdate：更新的时候执行的函数。
    # name：该属性在数据库中的字段映射。
    season_id = Column(Integer,primary_key = True, unique=True)
    media_id = Column(Integer,)
    badge = Column(String(20))
    badge_type = Column(Integer,)
    index_show = Column(String(20))
    is_finish = Column(Integer,)
    b_order = Column(String(20))
    order_type = Column(String(20))
    title = Column(String(50))
    title_icon = Column(String(130))
    cover = Column(String(130))
    link = Column(String(130))
    create_date = Column(DateTime, default=datetime.datetime.utcnow, name = "创建时间")
    update_time = Column(DateTime, default=datetime.datetime.utcnow, onupdate=func.now(), name = "修改时间")

    def __repr__(self):
        return '<Anime(season_id="{}", title="{}")>'.format(self.season_id, self.title)

def insert(data):
    # data type : [dict,dict...]
    # 插入数据
    for item in data:
        # 查找id是否在数据表里已存在
        temp = session.query(Anime).filter_by(season_id=item['season_id']).all()
        if temp:        # 如果已存在 则修改值 不存在就创建新数据
            new = temp[0]
            new.media_id = item['media_id']
            new.badge = item['badge']
            new.badge_type = item['badge_type']
            new.index_show = item['index_show']
            new.is_finish = item['is_finish']
            new.b_order = item['order']
            new.order_type = item['order_type']
            new.title = item['title']
            new.title_icon = item['title_icon']
            new.cover = item['cover']
            new.link = item['link']
        else:
            new = Anime(season_id = item['season_id'], media_id = item['media_id'], badge = item['badge'], badge_type = item['badge_type'],
                    index_show = item['index_show'], is_finish = item['is_finish'], b_order = item['order'], order_type = item['order_type'], 
                    title = item['title'], title_icon = item['title_icon'], cover = item['cover'], link = item['link']
                    )
            session.add(new)
        if debug:
            print("item --> ", new)
    session.commit()

def Create_table():
    # 创建数据表
    Base.metadata.create_all()
    print("table {} 创建成功".format(Anime.__tablename__))

if __name__ == "__main__":
    Create_table()