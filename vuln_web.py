#this prints the urls which may have sensitive information
from time import sleep
import bs4
import requests

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

vuln_data() #this is to get sample output, remove this function call and pass parameter in API