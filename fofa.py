import os
from traceback import format_exc
from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4

def write(ip_list):
    with open("ip_list.txt", "w") as f:
        for i in ip_list:
            f.write(i + "\n")
    print("ip写入成功")
def find(html):
    ip = bs4.BeautifulSoup(driver.page_source, "html.parser")
    ip = ip.find_all("span", attrs={"class": "hsxa-copy-btn"})

    for i in ip:
        src = i.get("data-clipboard-text")
        if src in ip_list:
            continue
        else:
            ip_list.append(src)
    print("ip添加成功")
ip_list = []
fofa_search=input("请输入你的fofa语句：")

# 创建 ChromeOptions 对象
chrome_options = Options()

chrome_options.add_argument("--user-data-dir=C:\\Users\\(用户名)\\AppData\\Local\\Google\\Chrome\\User Data")
chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222")

service = Service(ChromeDriverManager().install())
# 创建 Chrome WebDriver 实例，将 options 作为关键字参数传入
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://fofa.info/")
search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".custom-textarea.blurred.indexAutoComplete"))
)
search.send_keys(fofa_search)
search.send_keys(Keys.RETURN)
html = driver.page_source
find(html)
write(ip_list)
driver.quit()


