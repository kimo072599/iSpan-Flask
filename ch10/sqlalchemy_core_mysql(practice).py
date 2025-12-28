#----------practice start------------
import sqlalchemy as db
from urllib.parse import quote_plus

#連接資料庫
username = 'AIPE0213'     # 資料庫帳號
password = quote_plus('P@ssw0rd')     # 資料庫密碼
host = 'localhost'    # 資料庫位址
port = '3306'         # 資料庫埠號
database = 'classicmodels'   # 資料庫名稱
table = 'offices'   # 表格名稱
# 建立資料庫引擎
engine = db.create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')
# 建立資料庫連線
# con = engine.raw_connection()
connection  = engine.connect()

# 取得資料庫的元資料（資料庫預設編碼、表格清單、表格的欄位與型態、... 等）
metadata = db.MetaData()
print(f"metadata: \n{metadata.sorted_tables}")

# 取得 office 資料表的 Python 對應操作物件
table_office = db.Table(table, metadata, autoload_with=engine)
print(f"metadata: \n{metadata.sorted_tables}",end="\n"+("-"*80)+"\n")  # 比較Table建立前後的metadata 

# SELECT fetchall
query = db.select(table_office).select_from(table_office)
proxy = connection.execute(query)
results = proxy.fetchall()
print(results,end="\n"+("-"*80)+"\n")

#----------practice end--------------


