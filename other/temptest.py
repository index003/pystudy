import requests

# 主站顶部导航栏
url2 = 'https://api.bitgame.com/sp/maintain/config/list'
res = requests.get(url2)
print(res.text)

# 赛事类别信息
url3 ='https://api.bitgame.com/lottery/platform/menus?lang=zh-Hant&type=0&launchType=CENTRALIZED'
res = requests.get(url3)
print(res.text)

# 赛事频道首页 热门精选赛事列表
url4 = 'https://api.bitgame.com/lottery/platform/v2/matches?type=0&subType=1&lang=zh-Hant&launchType=CENTRALIZED'
res = requests.get(url4)
print(res.text)

# 赛事频道首页 最近24小时赛事列表
url5 = 'https://api.bitgame.com/lottery/platform/v2/matches?type=0&subType=2&lang=zh-Hant&launchType=CENTRALIZED'
res = requests.get(url5)
print(res.text)

# 赛事频道 足球页 早盘 热门精选赛事列表
url6 = 'https://api.bitgame.com/lottery/platform/v2/matches?type=1&subType=1&categoryId=8&lang=zh-Hant&launchType=CENTRALIZED'
res = requests.get(url6)
print(res.text)

# 赛事频道 足球页 早盘 最近24小时赛事列表
url7 = 'https://api.bitgame.com/lottery/platform/v2/matches?type=1&subType=2&categoryId=8&lang=zh-Hant&launchType=CENTRALIZED'
res = requests.get(url7)
print(res.text)

# 赛事频道 足球页 早盘 全部赛事列表
url8 = 'https://api.bitgame.com/lottery/platform/v2/matches?type=1&subType=0&categoryId=8&lang=zh-Hant&launchType=CENTRALIZED'
res = requests.get(url8)
print(res.text)

# 赛事频道 足球页 早盘 联赛赛事列表
url9 = 'https://api.bitgame.com/lottery/platform/v2/matches?type=1&subType=0&leagueId=13945&lang=zh-Hant&launchType=CENTRALIZED'
res = requests.get(url9)
print(res.text)

