import string
from fastapi import FastAPI
from username import username_find
from vuln_web import vuln_data
from website import website_details
import bs4 
import requests
from bs4 import BeautifulSoup
app = FastAPI()


@app.get("/username")
def username_find(name: string):
    
    sites=["facebook.com ", "linkedin.com ", "instagram.com ", "twitter.com ", "github.com ", "reddit.com ", "twitch.com ", "tumblr.com "]

    searchquery = "https://www.google.com/search?q=site:"
    for i in sites:
        url = searchquery+i+name
        page = requests.get(url) #runs the query on google
        soup = BeautifulSoup(page.text, 'html.parser')
        heading_object=soup.find_all( 'h3' )

        print("\nRelated searches for"+i+": \n")
        for info in heading_object:
            print(info.getText())
            print("------")

@app.get("/web_detail")
def website_details(website_name):#the website name must be  WITHOUR .com
    searchstart = "https://www.google.com/search?q=site:"


    key = [".com intitle:admin", """.com intitle:"index of/"" *.csv""", """.com intitle:"index of" *.apk""", ]

    for i in key:
        searchquery = searchstart+website_name+i
        request_result=requests.get( searchquery )
        soup = bs4.BeautifulSoup(request_result.text,"html.parser") 

        heading_object=soup.find_all( 'h3' )
        urls = soup.find_all('a', href=True)

        print("\nRelated search tags: \n")#prints h3 tags
        for info in heading_object:
            print(info.getText())
            print("------")

        print("\nrelated urls: \n")#prints urls
        for det in urls:
            print(det.get('href')) 

@app.get("/vul_data")
def vuln_data():#no parameter, once user clicks the general vulnerable urls print   
    searchstart = "https://www.google.com/search?q=site:"

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
            print(det.get('href'))
