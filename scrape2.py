import requests
from bs4 import BeautifulSoup
import json

    

url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"#網址


response = requests.get(url)#使用 requests.get() 發送 http get 請求
response.encoding = 'utf-8'#設定編碼為utf-8

if response.status_code == 200:#狀態碼檢查
    print("請求成功!")
else:
    print("請求失敗，狀態碼：", response.status_code)


html_content = response.text#取得html原始碼字串


soup = BeautifulSoup(html_content,"lxml")#使用BeautifulSoup解析html
books = soup.find_all("article", class_="product_pod")#找出所有書本的article標籤，並篩選class為product_pod
books_data = []#建一個空列表用來儲存
for book in books:

    #找書名:先找h3標籤，再找a標籤，再找title屬性
    title = book.find("h3").find("a").get("title")

    #找價格:找p標籤，再找class屬性為price_color，再取文字
    price = book.find("p",class_="price_color").text

    #找評分:找p標籤，再找class屬性為star-rating，取class陣列的第二個元素
    rating = book.find("p", class_="star-rating").get("class")[1]

    #將書本的資料加入列表
    books_data.append({
        "title": title,
        "price": price,
        "rating": rating
    })

#印出書籍資料，json.dumps會把python資料轉乘JSON字串，indent=2表示每層縮排2個空格，ensure_ascii=False表示保留原本字元
print(json.dumps(books_data, ensure_ascii=False, indent=2))

#將資料寫進JSON檔，並保持編碼和縮排
with open("travel_books.json", "w", encoding = "utf-8") as f:
    json.dump(books_data, f, ensure_ascii = False, indent = 2)

