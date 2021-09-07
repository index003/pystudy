import requests

url = 'https://fat1-api.testbitgame.com/lottery/platform/contract_bet_logs'

data = {
    "userAddress": "TXXRnHSka4RSKn6d6DvcWVbCiTrDNEvs78999999",
    'amount': 10,
    "currency": "TRX",
    "optionId": 222719,
    "odds": 2.18,
    "platform":2
}

header = {
    'content-type': 'application/json;charset=UTF-8'
}

for run_times in range(20):
    res = requests.post(url, json=data, headers= header)
    print(res.text)
