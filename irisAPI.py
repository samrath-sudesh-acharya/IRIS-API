from cgitb import text
from fastapi import FastAPI
from username import username_find
from vuln_web import vuln_data
from website import website_details
import bs4 
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
app = FastAPI()


@app.get("/username={name}")
def username_find(name: str):
    data = []
    sites=["facebook.com ", "linkedin.com ", "instagram.com ", "twitter.com ", "github.com ", "reddit.com ", "twitch.com ", "tumblr.com "]

    searchquery = "https://www.google.com/search?q=site:"
    for i in sites:
        url = searchquery+i+name
        page = requests.get(url) #runs the query on google
        soup = BeautifulSoup(page.text, 'html.parser')
        heading_object=soup.find_all( 'h3' )
        link = soup.find_all('a',href=True)
        for i in link :
            print(i)
        print(link)
        for info in heading_object:
            # print(info.getText())
            data.append({"site":i,"info":info.getText()})
            # print("------")
    # print(link)
    
    return data

@app.get("/web_detail={website_name}")
def website_details(website_name:str):#the website name must be  WITHOUR .com
    data = []
    searchstart = "https://www.google.com/search?q=site:"


    key = [" intitle:admin", """ intitle:"index of/"" *.csv""", """ intitle:"index of" *.apk""", ]

    for i in key:
        searchquery = searchstart+website_name+i
        print(searchquery)
        request_result=requests.get( searchquery )
        soup = bs4.BeautifulSoup(request_result.text,"html.parser") 

        heading_object=soup.find_all('h3')
        urls = soup.find_all('a', href=True)
        print(heading_object)
        print("\nRelated search tags: \n")#prints h3 tags
        for info in heading_object:
            print(info.getText())
            print("------")

        print("\nrelated urls: \n")#prints urls
        for det in urls:
            if(heading_object==[]):
                data.append({"link":det.get('href')})
            else:
                data.append({"title": info.getText(),"link":det.get('href')})
    return data

         

@app.get("/vul_data")
def vuln_data():#no parameter, once user clicks the general vulnerable urls print   
    searchstart = "https://www.google.com/search?q=site:"
    data = []
    key = ["""*.id intitle:"index of" "screenshot*.jpg" """, """ .edu intext:"index of" "payroll" """, """intitle:"index of" "apache.log" | "apache.logs" """]

    for i in key:
        searchquery = searchstart+i
        request_result=requests.get( searchquery )
        soup = bs4.BeautifulSoup(request_result.text,"html.parser") 

        heading_object=soup.find_all( 'h3' )
        urls = soup.find_all('a', href=True)

        print("Related searches: ")
        for info in heading_object:
            print(info.getText())
            print("------")

        print("related urls: ")
        for det in urls:
            data.append({"url":det.get('href')})
    return data

@app.get("/ip={ip}")
def scan_ip(ip:str):
    res = requests.get(f'https://ipinfo.io/{ip}')
    soup = BeautifulSoup(res.text,'html.parser')
    return soup.text

@app.get("/phone_number={ph}")
def phone_number(ph:str):
    

    chromedriver_autoinstaller.install()
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(10)
    driver.get('https://www.findandtrace.com/trace-mobile-number-location')
    driver.find_element(By.XPATH,'//*[@id="searchbox"]').send_keys(f'{ph}')
    f = driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div/div[1]/div/form/input[2]').send_keys(Keys.ENTER)
    table = driver.find_elements(By.CLASS_NAME,'shop_table')
    return {"data":table[0].text+table[1].text}

origins = ["*"]

app = CORSMiddleware(
    app=app,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)