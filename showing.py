# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
im

f=open(r'cookies.txt','r')#打开所保存的cookies内容文件
cookies={}#初始化cookies字典变量
for line in f.read().split(';'):   #按照字符：进行划分读取
    #其设置为1就会把字符串拆分成2份
    name,value=line.strip().split('=',1)
    cookies[name]=value  #为字典cookies添加内容
#取到第一条广播
url="https://www.douban.com/people/zshowing/statuses"
headers={"Content-Type":"text/html; charset=utf-8"}
r=requests.get(url,headers=headers,cookies=cookies,verify=False)
html=str(r.content,'utf-8')


soup = BeautifulSoup(''.join(html))

blockquote = soup.find('blockquote')


firstBlockquote=soup.find('blockquote')

print(firstBlockquote.get_text())


#每隔100s查询一下广播列表，如果有更新则在自己的帐号添加一条广播
while(True):
    url1 = "https://www.douban.com/people/zshowing/statuses"
    url2="https://frodo.douban.com/api/v2/status/create_status"
    data={
        'ck':'UGny',
        'note_id':640943262,
        'note_title':'d',
        'note_text':'11test',
        'author_tags':'',
        'note_privacy':'X',
        'captcha-solution':'other',
        'captcha-id':'zRtetxKalBKRNeE76ajNNGBL%3Aen'
    }

    headers1 = {"Content-Type": "application/x-www-form-urlencoded", "User-Agent":"api-client/0.1.3 com.douban.frodo/5.9.0 iOS/8.1.3 iPhone5,2 network/wifi", "Authorization": "Bearer 9ad784f32abce67ad0868ed98036b36e"}
    headers = {"Content-Type": "text/html; charset=utf-8"}
    r = requests.get(url1, headers=headers, cookies=cookies, verify=False)
    html = str(r.content, 'utf-8')
    newSoup = BeautifulSoup(''.join(html))
    newFirstBlockquote = newSoup.find('blockquote')
    if newFirstBlockquote.get_text()==firstBlockquote.get_text():

        print("no update")
        print(newFirstBlockquote.get_text())

    else:
        print('又有新更新啦！')
        data1 = {
            '_sig': 'cEQKEqKlCzOnzZ6FRbTkf10atsk%3D',
            '_ts': int(time.time()),
            'alt': 'json',
            'apikey': '0ab215a8b1977939201640fa14c66bab',
            'douban_udid': 'e84e6d2ddc940413f694189337ae15abe20fefe1',
            'latitude': 39.91667,
            'loc_id': 108288,
            'longitude': 116.41667,
            'text': "老哥的广播："+newFirstBlockquote.get_text(),
            'udid': '1792e7e8a3aef49f3a63dbbf8e4ce8cc633ceacc',
            'version': '5.9.0'
        }
        m = requests.post(url2, data=data1, headers=headers1, cookies=cookies, verify=False, allow_redirects=True)
        print(m.content)
        firstBlockquote = newFirstBlockquote
    time.sleep(100)


