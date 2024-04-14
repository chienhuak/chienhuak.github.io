print()
print("#Task 1-1 (優化):新增支線情況")

stations = [{"n":'Xindian',"idx":0}, {"n":'Xindian City Hall',"idx":1}, {"n":'Qizhang',"idx":2}, {"n":'Dapinglin',"idx":3},
            {"n":'Xiaobitan',"idx":1, "branch":"Qizhang"}, {"n":'Jingmei',"idx":4},{"n":'Wanlong',"idx":5}, {"n":'Gongguan',"idx":6},
            {"n":'Taipower Building',"idx":7}, {"n":'Guting',"idx":8}, {"n":'Chiang Kai-Shek Memorial Hall',"idx":9},
            {"n":'Xiaonanmen',"idx":10}, {"n":'Ximen',"idx":11}, {"n":'Beimen',"idx":12}, {"n":'Zhongshan',"idx":13},
            {"n":'Songjiang Nanjing',"idx":14}, {"n":'Nanjing Fuxing',"idx":15}, {"n":'Taipei Arena',"idx":16},
            {"n":'Nanjing Sanmin',"idx":17}, {"n":'Songshan',"idx":18}]


def distance(s, t):   # s:start t:destination
  #s = next((x for x in stations if x["n"]==staA), None)
  #t = next((x for x in stations if x["n"]==staB), None)
  sb=None
  tb=None
  if "branch" in s :
    sb = next((x for x in stations if x["n"]==s["branch"]), None)
  if "branch" in t:
    tb = next((x for x in stations if x["n"]==t["branch"]), None)

  if sb is None:
    if tb is None:
      return abs(s["idx"]-t["idx"])
    else:
      return abs(s["idx"]-tb["idx"])+t["idx"]
  else:
    if tb is None:
      return abs(sb["idx"]-t["idx"])+s["idx"]
    else:
      return abs(sb["idx"]-tb["idx"])+s["idx"]+t["idx"]


def find_and_print_plus(messages, current_station):
  start_info = next((x for x in stations if x["n"]==current_station), None)
  #print(start_info)
  msg_info = [{'name':x, 'current_station':next((s for s in stations if messages[x].find(s["n"])>=0), None)} for x in messages]
  #print(msg_info)
  near = min(msg_info, key=lambda x: distance(x["current_station"],start_info))
  print(near["name"])

    
messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}
    
find_and_print_plus(messages, "Wanlong") # print Mary
find_and_print_plus(messages, "Songshan") # print Copper
find_and_print_plus(messages, "Qizhang") # print Leslie
find_and_print_plus(messages, "Ximen") # print Bob
find_and_print_plus(messages, "Xindian City Hall") # print Vivian
find_and_print_plus(messages, "Dapinglin") # print Mary


print()
print("#Task 1:最近的車站")


def find_and_print(messages, current_station):
  # your code here
  stations = ['Xindian','Xindian City Hall','Qizhang','Xiaobitan','Dapinglin','Jingmei','Wanlong','Gongguan','Taipower Building','Guting','Chiang Kai-Shek Memorial Hall','Xiaonanmen','Ximen','Beimen','Zhongshan','Songjiang Nanjing','Nanjing Fuxing','Taipei Arena','Nanjing Sanmin','Songshan']
  
  # 創建一個新的字典來存儲每個人的名字和對應的地點
  new = {}
  myloc = stations.index(current_station)

  # 比對每條訊息中是否包含在stations中的值
  for name, message in messages.items():
    for station in stations:
        if station in message:
            new[name] = station 


  # 創建一個新的字典來存儲每個人的名字和對應的索引
  indexes = {}

  # 遍歷new字典中的每一對鍵值對
  for name, location in new.items():
    # 使用index()方法找到location在stations列表中的索引
    index = stations.index(location)
    indexes[name] = index


  # 創建一個新的字典來存儲每個人的名字和與iloc之間的距離
  desc = {}

  # 遍歷indexes字典中的每一對鍵值對
  for name, index in indexes.items():
    # 計算每個人的索引與iloc之間的距離，並將結果存儲到desc字典中
    distance = abs(index - myloc)
    desc[name] = distance

  # 找到desc字典中最小值對應的鍵
  min_distance_name = min(desc, key=desc.get)
  print(min_distance_name)

messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}
find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian


print()
print("#Task 2:預定當天諮詢、依條件推薦合適顧問")


consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]


for i in consultants:
  i['time']=[]
# your code here, maybe
def book(consultants, hour, duration, criteria):
  # your code here

  #找到有空的顧問
  avaliable = [consultant['name'] for consultant in consultants]
  for t in range (hour,hour+duration):
    for n in consultants:
      #print(n)
      #print(n['time'])
      if t in n['time'] and n['name'] in avaliable:
        avaliable.remove(n['name'])

  #如果沒有顧問有空
  if avaliable ==[]:
    print("No Service")
    return  # 終止函數
  
  
  #print(avaliable)


  #判斷"價格"條件
  if criteria == "price":
    prices = [consultant['price'] for consultant in consultants if consultant['name'] in avaliable] #找出avaliable顧問價格
    min_price = min(prices) #比較最低價格
    for x in consultants:
      if x["price"] == min_price:
        x["time"].append(hour)  #將預定時間加到指定顧問資料裡
        if duration > 1:
          for t in range (1,duration): 
            hour += 1           
            x["time"].append(hour)
            
        print(x["name"])

    #print(consultants)

  #判斷"評價"條件
  if criteria == "rate":
    rates = [consultant['rate'] for consultant in consultants if consultant['name'] in avaliable] #找出avaliable顧問評價
    max_rate = max(rates) #比較最高評價
    for x in consultants:
      if x["rate"] == max_rate:
        x["time"].append(hour)  #將預定時間加到指定顧問資料裡
        if duration > 1:
          for t in range (1,duration): 
            hour += 1           
            x["time"].append(hour)
            
        print(x["name"])
    
    #print(consultants)



book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John


print()
print("#Task 3:尋找中間名進行比對")

    
def func(*data):
    # your code here
    rule = ["",2,2,3,3]
    name_num = []
    middle= []
    for i in range (0,len(data)):
        name_num += [rule[len(data[i])-1]] 
        middle += [data[i][name_num[i]-1]]
    unique_value = [x for x in middle if middle.count(x) == 1]
    
    if unique_value == []:
        print("沒有")
    else:
        index = middle.index(unique_value[0])
        print(data[index])


func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安    
    
    
    
print()
print("#Task 4:尋找數列規則 0, 4, 8, 7, 11, 15, 14, 18, 22, 21, 25, ...")


def get_number(index):
    # your code here
    formula = lambda index: (index-index//3)*4 + (-1)*(index//3)
    print(formula(index))
        
        
  
get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70



print()
print("#Task 5 (Optional):訂車票")



def find(spaces, stat, n):
  # your code here
  for i in range(0,len(spaces)):
    if stat[i] == 0:
      spaces[i] = 0

  check = False
  for j in spaces:
    if j>=n:
      print(spaces.index(j))
      check = True
      break

  if check == False:
    print(-1)
  
  #print(spaces)
find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2