import cx_Oracle
from sqlalchemy import create_engine

host='illin659'
port=1521
sid='dmcnv'
user='soumyakp'
password='soumyakp'
sid = cx_Oracle.makedsn(host, port, sid=sid)

cstr = 'oracle://{user}:{password}@{sid}'.format(
    user=user,
    password=password,
    sid=sid
)

# Create a oracle engine instance
engine =  create_engine(
    cstr,
    convert_unicode=False,
    pool_recycle=10,
    pool_size=50,
    echo=True
)
