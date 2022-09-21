#prints the username for the below 8 websites
from asyncio.windows_events import NULL
from operator import contains
import string
from urllib import response
from tkinter import Y
from bs4 import BeautifulSoup
import requests
# site1 = "facebook.com"
# site2 = "linkedin.com"
# site3 = "instagram.com"
# site4 = "twitter.com"
# site5 = "github.com"
# site6 = "reddit.com"
# site7 = "twitch.com"
# site8 = "tumblr.com"
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
    
#***Add this if your want to print user urls also(not recommended)***
    # print("Related urls")
    # for link in soup.find_all('a', href = True):
    #     print(link.get('href'))

# x = input("user name goes here: ") #this is to get sample output, remove this line and pass parameter in API
# username_find(x)