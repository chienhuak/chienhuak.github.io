import urllib.request as req
import bs4

# 定義函數，用於爬取指定頁面的內容
def crawl_page(url):
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
        "cookie": "over18=1;"
    })
    with req.urlopen(request) as response:
        return response.read().decode("utf-8")

url = "https://www.ptt.cc/bbs/Lottery/index.html"

# 爬取第一頁到第三頁的內容
for page_number in range(1, 4):
    ptt = crawl_page(url)
    soup = bs4.BeautifulSoup(ptt, "html.parser")

    urls = soup.find_all("a", class_="btn wide")
    if urls:
      url = "https://www.ptt.cc" + urls[1]['href']
      #print(url)



    # 初始化列表
    title_data = []
    like_data = []
    time_data = []

    # 取得標題、點擊數和時間
    titles = soup.find_all("div", class_="title")
    for title in titles:
        if title.a is not None:
            title_data.append(title.a.string)

            herf = title.a['href']
            title_urls = "https://www.ptt.cc" + herf
            article = crawl_page(title_urls)
            soupX = bs4.BeautifulSoup(article, "html.parser")

            meta_values = soupX.find_all("span", class_="article-meta-value")
            if meta_values:
                last_meta_value = meta_values[-1].text.strip()
            else:
                #pass
                last_meta_value = "(沒時間)"
            time_data.append(last_meta_value)
            #print(title.a.string,title_urls,last_meta_value,meta_values)
        else:
            title_data.append("(本文已被刪除)")
            time_data.append("(本文已被刪除)")
            

    likes = soup.find_all("div", class_="nrec")
    for like in likes:
        if like.span is not None:
            like_data.append(like.span.string)
        else:
            like_data.append("0")

    # 目標輸出串一起，存成 article.csv
    csv_file = 'article.csv'

    # 寫入 CSV 文件
    with open(csv_file, 'a') as f:
        for i in range(len(like_data)):
            try:
                if '[情報]' in title_data[i]:
                    time_data.insert(i, '([情報]沒有時間)')
                    
                if '刪除' not in title_data[i]:
                  line = ",".join([title_data[i], like_data[i], time_data[i]]) + '\n'
                f.write(line)
            except KeyError as e:
                print(f"KeyError occurred: {e}. Skipping this row.")

print("CSV 文件已創建成功！")
