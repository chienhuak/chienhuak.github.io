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



#我需要的資訊`:
#捷運站名 MRT
#地址(行政區) address
#景點名 stitle
#捷運站 info
#地圖座標 longitude + latitude


mrts = [{'MRT': '文德', 'SERIAL_NO': '2011051800000646', 'address': '臺北市  內湖區內湖路2段175號'}, {'MRT': '中正紀念堂', 'SERIAL_NO': '2011051800000096', 'address': '臺北市  中正區南海路49號'}, {'MRT': '關渡', 'SERIAL_NO': '2011051800000049', 'address': '臺北市  士林區菁山路101巷170號'}, {'MRT': '西門', 'SERIAL_NO': '2011051800000352', 'address': '臺北市  萬華區成都路10號'}, {'MRT': '松山', 'SERIAL_NO': '2011051800000300', 'address': '臺北市  松山區八德路4段761號'}, {'MRT': '關渡', 'SERIAL_NO': '2011051800000320', 'address': '臺北市  北投區知行路360號'}, {'MRT': '北投', 'SERIAL_NO': '2011051800000199', 'address': '臺北市  北投區幽雅路32號'}, {'MRT': '葫洲', 'SERIAL_NO': '2011051800000655', 'address': '臺北市  內湖區康樂街'}, {'MRT': '臺大醫院', 'SERIAL_NO': '2011051800000137', 'address': '臺北市  中正區臺北市懷寧街、襄陽路、公園路、凱達格蘭大道口'}, {'MRT': '劍潭', 'SERIAL_NO': '2011051800000100', 'address': '臺北市  士林區士商路189號'}, {'MRT': '木柵', 'SERIAL_NO': '2011051800000272', 'address': '臺北市  文山區萬壽路115號'}, {'MRT': '忠孝新生', 'SERIAL_NO': '2011051800000377', 'address': '臺北市  中山區八德路2段85號'}, {'MRT': '市政府', 'SERIAL_NO': '2012032000000001', 'address': '臺北市  信義區光復南路133號'}, {'MRT': '圓山', 'SERIAL_NO': '2011051800000260', 'address': '臺北市  大同區哈密街61號'}, {'MRT': '芝山', 'SERIAL_NO': '2011051800000041', 'address': '臺北市  士林區士林橋'}, {'MRT': '劍潭', 'SERIAL_NO': '2011051800000120', 'address': '臺北市  北投區陽明路2段15號'}, {'MRT': '龍山寺', 'SERIAL_NO': '2011051800000364', 'address': '臺北市  萬華區廣州街101號'}, {'MRT': '公館', 'SERIAL_NO': '2011051800000125', 'address': '臺北市  中正區思源街1號'}, {'MRT': '新北投', 'SERIAL_NO': '2011051800000061', 'address': '臺北市  北投區中山路、光明路沿線'}, {'MRT': '雙連', 'SERIAL_NO': '2011051800000007', 'address': '臺北市  大同區環河北路一段'}, {'MRT': '士林', 'SERIAL_NO': '2011051800000129', 'address': '臺北市  士林區福林路60號'}, {'MRT': '士林', 'SERIAL_NO': '2011051800000092', 'address': '臺北市  士林區至善路二段221號'}, {'MRT': '新北投', 'SERIAL_NO': '2011051800000693', 'address': '臺北市  北投區光明路251號'}, {'MRT': '圓山', 'SERIAL_NO': '2011051800000037', 'address': '臺北市  士林區基隆河左、右岸'}, {'MRT': '大湖公園', 'SERIAL_NO': '2011051800000642', 'address': '臺北市  內湖區成功路5段31號'}, {'MRT': '大直', 'SERIAL_NO': '2011051800000116', 'address': '臺北市  中山區北安路139號'}, {'MRT': '關渡', 'SERIAL_NO': '2011051800000011', 'address': '臺北市  北投區關渡碼頭'}, {'MRT': '劍潭', 'SERIAL_NO': '2011051800000033', 'address': '臺北市  士林區延平北路七段'}, {'MRT': '石牌', 'SERIAL_NO': '2011051800000086', 'address': '臺北市  士林區中山北路7段232巷'}, {'MRT': '中山', 'SERIAL_NO': '2011051800000141', 'address': '臺北市  大同區長安西路39號'}, {'MRT': '中山', 'SERIAL_NO': '2011051800000158', 'address': '臺北市  中山區中山北路2段18號'}, {'MRT': '圓山', 'SERIAL_NO': '2011051800000133', 'address': '臺北市  中山區中山北路3段181號'}, {'MRT': '忠義', 'SERIAL_NO': '2011051800000584', 'address': '臺北市  北投區中央北路4段18巷50號'}, {'MRT': '動物園', 'SERIAL_NO': '2011051800000025', 'address': '臺北市  文山區木柵路'}, {'MRT': '松江南京', 'SERIAL_NO': '2011051800000244', 'address': '臺北市  中山區建國北路1段 96 號 B1'}, {'MRT': '雙連', 'SERIAL_NO': '2011051800000432', 'address': '臺北市  萬華區華中二疏散門入口'}, {'MRT': '新北投', 'SERIAL_NO': '2011051800000660', 'address': '臺北市  北投區中山路2號'}, {'MRT': '中山', 'SERIAL_NO': '2011051800000292', 'address': '臺北市  大同區迪化街1段61號'}, {'MRT': '國父紀念館', 'SERIAL_NO': '2011051800000112', 'address': '臺北市  信義區仁愛路4段505號'}, {'MRT': '士林', 'SERIAL_NO': '2011051800000567', 'address': '臺北市  士林區竹子湖路1-20號(陽明山國家公園管理處)'}, {'MRT': '動物園', 'SERIAL_NO': '2011051800000689', 'address': '臺北市  文山區新光路二段30號'}, {'MRT': '劍潭', 'SERIAL_NO': '2011051800000057', 'address': '臺北市  北投區竹子湖路1之20號'}, {'MRT': '唭哩岸', 'SERIAL_NO': '2011051800000029', 'address': '臺北市  北投區關渡'}, {'MRT': '大安森林公園', 'SERIAL_NO': '2011051800000574', 'address': '臺北市  大安區新生南路以東、信義路3段以南'}, {'MRT': '新北投', 'SERIAL_NO': '2011051800000685', 'address': '臺北市  北投區中山路'}, {'MRT': '象山', 'SERIAL_NO': '2011051800000550', 'address': '臺北市  信義區信義路五段150巷'}, {'MRT': '龍山寺', 'SERIAL_NO': '2011051800000288', 'address': '臺北市  萬華區廣州街211號'}, {'MRT': '行天宮', 'SERIAL_NO': '2011051800000276', 'address': '臺北市  中山區民權東路2段109號'}, {'MRT': '新北投', 'SERIAL_NO': '2011051800000676', 'address': '臺北市  北投區中山路6號'}, {'MRT': '中正紀念堂', 'SERIAL_NO': '2011051800000108', 'address': '臺北市  中正區中山南路21號'}, {'MRT': '市政府', 'SERIAL_NO': '2011051800000186', 'address': '臺北市  信義區市府路1號1-4樓'}, {'MRT': '動物園', 'SERIAL_NO': '2011051800000557', 'address': '臺北市  文山區指南路三段33巷'}, {'MRT': '新北投', 'SERIAL_NO': '2011051800000145', 'address': '臺北市  北投區中山路二號'}, {'MRT': '關渡', 'SERIAL_NO': '2011051800000205', 'address': '臺北市  北投區中央北路四段515巷16號'}, {'MRT': '忠孝新生', 'SERIAL_NO': '2011051800000424', 'address': '臺北市  中正區八德路1段1號'}, {'MRT': '臺大醫院', 'SERIAL_NO': '2011051800000596', 'address': '臺北市  中正區中山南路11號'}, {'MRT': '台北101／世貿', 'SERIAL_NO': '2011051800001090', 'address': '臺北市  信義區信義路5段7號'}, {'MRT': '龍山寺', 'SERIAL_NO': '2012021000000001', 'address': '臺北市  萬華區萬大路底華中橋旁'}]
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

#對每一個景點
for i in range (0,len(mrts)):
  mrts[i]["atts"]=[]

for att in attractions:
  try:
    #print(att)
    for i in range (0,len(mrts)):
      if mrts[i]["MRT"]==att["mrt"]:
        mrts[i]["atts"].append(att["stitle"])

  except KeyError as e:
    print(f"KeyError occurred: {e}. Skipping this row.")



#設置要寫入的CSV文件名稱
mrt_csv_file = 'mrt.csv'

#打開CSV文件並寫入數據   #with open(filename, mode)

with open(mrt_csv_file, 'w') as f:
    for row in mrts:
      try:
        #atts_str = ", ".join(row["atts"])
        line = f"{row['MRT']}, {', '.join(row['atts'])}" + '\n'
        print(line)
        f.write(line)
      except KeyError as e:
        print(f"KeyError occurred: {e}. Skipping this row.")

print(mrts)
print("mrt.csv 文件已創建成功！")



