from datetime import timedelta
from borax.calendars import LunarDate


# 获取今天的农历日期（农历2018年七月初一）
print(LunarDate.today())  # LunarDate(2018, 7, 1, 0)

# 将公历日期转化为农历日期
ld = LunarDate.from_solar_date(2013, 1, 23)
print(ld)  # LunarDate(2018, 7, 1, 0)
print(ld.strftime('%Y年%L%M月%D'))  # '二〇一八年六月廿六'
print(ld.strftime('今天的干支表示法为：%G'))  # '今天的干支表示法为：戊戌年庚申月辛未日'

# 日期推算，返回10天后的农历日期
print(ld.after(10))  # LunarDate(2018, 7, 11, 0)

# 可以直接与 datetime.timedelta 直接相加减
print(ld + timedelta(days=10))  # LunarDate(2018, 7, 11, 0)

today = LunarDate.today()
print(today.strftime('%Y年%L%M月%D'))  # '二〇一八年六月廿六'
print(today.strftime('今天的干支表示法为：%G'))  # '今天的干支表示法为：戊戌年庚申月辛未日'

for i in range(1, 5):
    print(i)