import requests
from lxml import etree
import re
import math

url="http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/74d63812e5b327d850ab4a8782833d47.svg"
url1="http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/c5697f4d7ed96370c8ebc32f80eeb20a.css"
print(requests.get(url).text)
html=requests.get(url).text
content_lists=re.findall("<textPath.*?>(.*?)</textPath>",html)
print(content_lists)
print(requests.get(url1).text)
html1=requests.get(url1).text
html1=html1.replace('"','')
key_lists=re.findall('\.(g.*?){background:-(.*?)\.0px -(.*?)\.0px;}',html1,re.S)
print(key_lists)
print(type(key_lists))

print(len(content_lists))
for i in range(len(content_lists)):
    print(i+1,content_lists[i])

lists={}
for i in range(len(key_lists)):
    print(i+1)
    print('{}'.format(key_lists[i][0]))
    print(round(int(key_lists[i][2]))/(3189/81)-1)
    print(round(int(key_lists[i][1])/14))
    try:
        if content_lists[round(int(key_lists[i][2])/(3189/81))-1][round(int(key_lists[i][1])/14)]:
            lists['{}'.format(key_lists[i][0])]=content_lists[round(int(key_lists[i][2])/(3189/81))-1][round(int(key_lists[i][1])/14)]
        else:
            lists['{}'.format(key_lists[i][0])] = content_lists[round(int(key_lists[i][2])/(3189/81))][round(int(key_lists[i][1])/14)]
    except:
        # lists['{}'.format(key_lists[i][0])] = content_lists[int(int(key_lists[i][2])/(3189/81))][round(int(key_lists[i][1])/14)]
        pass
print(lists)
