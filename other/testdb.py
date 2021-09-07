import pymysql

db =  pymysql.connect(host='172.16.4.41', port=3306, user='wuchangzheng', passwd='4SowuxTVU5pcE0pjb0uM', db='sport-lottery', charset='utf8')
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print(data)
sql = 'SELECT market_code,`names` FROM sport_market_config a where a.market_code LIKE "%INCLUDING_OVERTIME%"'
cursor.execute(sql)
data = cursor.fetchall()
# print(data)
for data_temp in data:
    print(data_temp[0])
    print(data_temp[1][-12:-2])

'''
MySQL表中存有bit型数据，相当于Python中的true和false类型数据，但是读取到的值是b'\x00'和b'\0x01'这两种
Python不会自动处理这种数据，需要进行转码才能实现后续的判断，刚开始以为这种数据类型是16进制，后来查询了一些资料发现利用Python自带方法ord()即可实现转码
'''
print(ord(b'\x01'))

cursor.close
db.close