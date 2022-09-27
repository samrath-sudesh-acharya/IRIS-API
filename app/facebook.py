from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.implicitly_wait(10)
start_url = "https://www.google.com/search?q="
google_url = "https://www.google.com/"
url = "https://m.facebook.com/public/Samrath"
driver.get(url)
SCROLL_PAUSE_TIME = 0.5
# Get scroll height
last_height = 11000
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height > last_height:
        user_name = driver.find_elements(By.TAG_NAME,'span')
        links = driver.find_elements(By.TAG_NAME,'a')
        break
driver.implicitly_wait(100)
link_list = []
user_list = []
for link in links:
    link_list.append(link.get_attribute("href"))
# user_name = [*set(user_name)] 

for user in user_name:
    user_list.append(user.text)

for i,j in zip(user_list[6:],link_list[6:]):
    print(i)
    print(j)
# input = driver.find_element(By.TAG_NAME,'input')
# input.send_keys("site:facebook.com rahul inurl:https://m.facebook.com/public/")
# input.send_keys(Keys.ENTER)