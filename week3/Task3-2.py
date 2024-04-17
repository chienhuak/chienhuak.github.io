# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 00:43:50 2024

@author: User
"""

import urllib.request as req
import bs4
#from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Lottery/index.html"

#建立 request 物件，附加 request headers 資訊 (模仿人類)
request = req.Request(url,headers={
    "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
    "cookie": "over18=1;"
})


with req.urlopen(request) as response :
  ptt = response.read().decode("utf-8")



soup = bs4.BeautifulSoup(ptt,"html.parser")  #整份網頁

title_data = [] #存放讀取到的資料
like_data = []
time_data = []

#ArticleTitle,Like/DislikeCount,PublishTime
#[問題] 享受輸的感覺539,4,Fri Jul 14 23:34:43 2023
#[報牌] 39樂合彩,0,Sat Jul 15 00:01:14 2023

#取得標題
titles = soup.find_all("div", class_="title")
for title in titles:    #ResultSet object has no attribute 'a'.
  if title.a is not None:   # if title.a != None
    #print(title.a.string)
    title_data.append(title.a.string)

    herf = title.a['href']
    title_urls = "https://www.ptt.cc" + herf
    request = req.Request(title_urls,headers={
    "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
    "cookie": "over18=1;"
    })
    with req.urlopen(request) as response :
      article = response.read().decode("utf-8")
    
    soupX = bs4.BeautifulSoup(article,"html.parser")
    
    # 找到所有具有 class="article-meta-value" 的元素
    meta_values = soupX.find_all("span", class_="article-meta-value")

    # 找到最後一個元素
    if meta_values:
        last_meta_value = meta_values[-1].text.strip()
        #print(last_meta_value)
        time_data.append(last_meta_value)
    else:
        #print("未找到具有 class=\"article-meta-value\" 的元素")
        #time_data.append("(本文已被刪除)")
        pass
    
  else:
    #print("No <a> tag found in this title.")
    title_data.append("(本文已被刪除)")
    time_data.append("(本文已被刪除)")
    #pass

#取得Like/DislikeCount
likes = soup.find_all("div", class_="nrec")
for like in likes:
  if like.span is not None:
    #print(like.span.string)
    like_data.append(like.span.string)
  else:
    #print("0")  #No <span> tag found in this article.
    like_data.append(0)



#目標輸出串一起，存成article.csv

#設置要寫入的CSV文件名稱
csv_file = 'article.csv'

#打開CSV文件並寫入數據   #with open(filename, mode)
with open(csv_file, 'w') as f:
    for i in range(0,len(like_data)):
      try:
        if '[情報]' in title_data[i]:
          time_data.insert(i, '([情報]沒有時間)')
        line = ",".join([title_data[i],str(like_data[i]),time_data[i]]) + '\n'
        f.write(line)
        
      except KeyError as e:
        print(f"KeyError occurred: {e}. Skipping this row.")

print("CSV 文件已創建成功！")