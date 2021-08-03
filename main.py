# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from bs4 import BeautifulSoup
import requests
r = requests.get("https://hi-news.ru/wp-content/uploads/2021/08/java_development_x5_group-650x358.jpg")

print(r.headers)

print(r.headers['last-modified'])
