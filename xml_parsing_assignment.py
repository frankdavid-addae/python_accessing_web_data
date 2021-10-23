from urllib import request
import xml.etree.ElementTree as ET

# Sample url
# http://py4e-data.dr-chuck.net/comments_42.xml

# Assignment url
# http://py4e-data.dr-chuck.net/comments_749547.xml

url = input('Enter URL: ')
xml = request.urlopen(url).read()

comments = ET.fromstring(xml)
counts = comments.findall('.//count')

total = 0

for item in counts:
    total += int(item.text)
print("Count: ", len(counts))
print("Sum: ", total)
