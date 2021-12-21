import pandas as pd
from icecream import  ic
import numpy as np
import MySQLdb
from sqlalchemy import create_engine

df = pd.read_csv("Result of 8177_Candidate.csv")
df_new = df.iloc[:,:4]
# ic(df_new.head(40))
df_new["Lib"] = np.nan
ic(df_new.head(40))

#
engine = create_engine('mysql+pymysql://root:320104Czy@127.0.0.1/umamidb?charset=utf8')
df_new.to_sql(name='umami_bitter_db', con=engine, if_exists='append',
            index=False)


# df_new.to_sql('umami_bitter_DB',con=engine,schema="umamidb",if_exists='append',index=False)


# 注释：
# fail（添加）：如果表存在，则不进行操作
# replace（覆盖）：如果表存在就删除表，重新生成，插入数据
# append（更新）：如果表存在就插入数据，不存在就直接生成表!


# host = '127.0.0.1'
# port = 3306
# db = 'umamidb'
# user = 'root'
# password = '320104Czy'
# engine = create_engine(str(r"mysql pymysql://%s:%s@%s/%s") % (user, password, host, db))