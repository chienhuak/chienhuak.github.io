# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:21:58 2024

@author: User
"""

import urllib.request as req
url1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
url2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"


with req.urlopen(url1) as response :
  attractions_json = response.read().decode("utf-8")

with req.urlopen(url2) as response :
  mrts_json = response.read().decode("utf-8")


#轉換資料格式
import json

attractions = json.loads(attractions_json)
attractions = attractions["data"]["results"]
#print(attractions)

mrts = json.loads(mrts_json)
mrts = mrts["data"]
#print(mrts)

#我需要的資訊`:
#捷運站名 MRT
#地址(行政區) address
#景點名 stitle
#捷運站 info
#地圖座標 longitude + latitude


for mrt in mrts:
  district = mrt["address"].split('  ')[1][:3]  #擷取出地址中的"行政區"
  mrt["district"] = district  #新增一個key放"MRT所在的行政區"
#print(mrts)


for att in attractions:
  for mrt in mrts:
    if mrt["MRT"] in att["info"]:
      att["mrt"] = mrt["MRT"]
      att["district"] = mrt["district"]  #景點中新增一個key放"行政區"
#print(attractions)


#取得第一個照片的ImageURL
for img in attractions:
  imgurl = "http"+img["filelist"].split('http')[1]
  img["imageurl"] = imgurl
  #print(imgurl)

#spot.csv 
#export format : SpotTitle,District,Longitude,Latitude,ImageURL
#export example : 新北投溫泉區,北投區,123.5446,24.5312,https://www.travel.taipei/pic/11000848.jpg

#設置要寫入的CSV文件名稱
csv_file = 'spot.csv'

#打開CSV文件並寫入數據   #with open(filename, mode)
with open(csv_file, 'w') as f: 
    for row in attractions:
      try:
        line = ",".join([row["stitle"],row["district"],row["longitude"],row["latitude"],row["imageurl"]]) + '\n'
        f.write(line)
      except KeyError as e:
        print(f"KeyError occurred: {e}. Skipping this row.")

print("spot.csv 文件已創建成功！")

#mrt.csv
#export format : StationName,AttractionTitle1,AttractionTitle2,AttractionTitle3,...
#export example : 新北投,新北投溫泉區,北投圖書館,地熱谷,...


#建一個不重複捷運站表+景點
uni_mrts = set()
for station in mrts:
    uni_mrts.add(station['MRT'])
    
uni_mrts_dict = {}
for mrt in uni_mrts:
    uni_mrts_dict[mrt] = {"atts": []}

#對每一個景點

for att in attractions:
    try:
        uni_mrts_dict[att["mrt"]]["atts"].append(att["stitle"])
    except KeyError as e:
        print(f"KeyError occurred: {e}. Skipping this row.")

#print(uni_mrts_dict)



#設置要寫入的CSV文件名稱
mrt_csv_file = 'mrt.csv'

#打開CSV文件並寫入數據   #with open(filename, mode)
with open(mrt_csv_file, 'w', encoding='utf-8') as f:
    #標題列
    f.write("MRT,Attractions\n")
    
    #每個捷運站景點
    for mrt, info in uni_mrts_dict.items():
        attractions = ", ".join(info["atts"])
        # 写入捷运站和景点列表
        line = f"{mrt},{attractions}\n"
        f.write(line)


# =============================================================================
# with open(mrt_csv_file, 'w') as f:
#     for row in mrts:
#       try:
#         #atts_str = ", ".join(row["atts"])
#         line = f"{row['MRT']}, {', '.join(row['atts'])}" + '\n'
#         print(line)
#         f.write(line)
#       except KeyError as e:
#         print(f"KeyError occurred: {e}. Skipping this row.")
# =============================================================================

#print(mrts)
print("mrt.csv 文件已創建成功！")



