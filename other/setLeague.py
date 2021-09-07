import requests

url = 'https://fat1-api-admin.testbitgame.com/lottery/leagues/libraryOrGrade/24011'
header = {
    'content-type': 'application/json',
    'authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTYyODYxMTI1NCwiY3JlYXRlZCI6MTYyODU2MDg1NDA1NiwiYXV0aG9yaXRpZXMiOltdfQ.nH9cbcH91b44uzKFmhPY707HLkTBGWZHSHk5WZy0TrcWkSTNtHtAftffHowTZs6acowD5z4b2q8qEXJmwpUQOQ'
}
data = {
    # 'grade': 'A',
    # 'location': 'INTERNATIONAL',
    'available':'true'
}

res = requests.patch(url, json=data, headers=header)
print(res.text)