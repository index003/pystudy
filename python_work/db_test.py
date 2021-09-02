# import db_util
#
# sql_list = [
#     "select * from sport_match_info where id = 1742",
#     "select * from sport_match_info where id = 1743",
#     "select * from sport_match_info where id = 1744"
# ]
#
# result = []
# for sql in sql_list:
#     result.append(db_util.query_execute(sql))
# print(result)
import mysql.connector


mydb = mysql.connector.connect(
    host='172.16.4.11',
    port=3306,
    user='wuchangzheng',
    passwd='JnbbSQj4kW6fLFDfZxlg',
    db='sport-lottery',
    charset='utf8'
)


mycursor = mydb.cursor()

sql = "delete from sport_market_change_info where match_id = 478;delete from sport_match_result_check where match_id = 478;"

mycursor.execute(sql, multi=True)

mydb.commit()

print(mycursor.rowcount, " 条记录删除")