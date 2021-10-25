import json
from urllib import request

# http://py4e-data.dr-chuck.net/comments_749548.json
# http://py4e-data.dr-chuck.net/comments_42.json

# url = 'http://py4e-data.dr-chuck.net/comments_749548.json'
url = input('Enter URL: ')
data = request.urlopen(url).read()
jsonData = json.loads(data)
comments = jsonData["comments"]
# print(comments)
totalCount = 0
for comment in comments:
    totalCount += comment["count"]
print(totalCount)

