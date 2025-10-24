import requests
import re

url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"#網址

#用requests
response = requests.get(url)#使用 requests.get() 發送 http get 請求
response.encoding = 'utf-8'
html_content = response.text#取得html原始碼字串

price_pattern = (r"£\d+\.\d{2}")#描述價錢的正規表示式

book_website_ip = re.findall(price_pattern,html_content)#re.findall 找出全部匹配的字串，並回傳為一個串列
print(book_website_ip)


if response.status_code == 200:#狀態碼檢查
    print("請求成功!")
else:
    print("請求失敗，狀態碼：", response.status_code)