import sqlalchemy

HOSTNAME  = "127.0.0.1"
PORT      = "3306"
DATABASE  = "clifford"
USERNAME  = "root"
PASSWORD  = "steamedbun"
DB_URI    = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

engine = sqlalchemy.create_engine(DB_URI)
l = []
with engine.connect() as con:
    rs = con.execute("select * from data")
    print(type(rs))
    count = 0
    for i in rs:
    #    count += 1
    #    print(count, i)
        l.append(i)