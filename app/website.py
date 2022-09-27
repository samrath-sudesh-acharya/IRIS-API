#when user enters input, this will give name and urls of potential vulnerability in them
import bs4
import requests

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

# webdemo = input("enter website name: ") #this is to get sample output, remove this line and pass parameter in API
# website_details(webdemo)