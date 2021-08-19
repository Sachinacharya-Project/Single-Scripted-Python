from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import os

os.system('cls')

myUrl = "https://www.flipkart.com/mobiles/~cs-lj5v0s4ukf/pr?sid=tyy%2C4io&collection-tab-name=narzo+20A&param=9123&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&sort=price_asc&otracker=clp_banner_1_7.bannerX3.BANNER_mobile-phones-big-diwali-sale-pl99i8k1-store_F8WVUJPE5HIX&fm=neo%2Fmerchandising&iid=M_9c2e8e9c-79e9-460e-9526-b244c1c4ee23_7.F8WVUJPE5HIX&ppt=clp&ppn=mobile-phones-big-diwali-sale-pl99i8k1-store&ssid=ejgmoky4000000001604837589535"
uClients = uReq(myUrl)
page_html = uClients.read()
uClients.close()

page_soup = soup(page_html, 'html.parser')

containers = page_soup.findAll('div', {"class": '_3O0U0u'})

titleDiv = containers[0].findAll('div', {'class': '_3wU53n'})
ratingDiv = containers[0].findAll('div', {'class': 'hGSR34'})
totalRatings = containers[0].findAll('span', {'class': '_38sUEc'})
#############################################################
# RESULTS OUTCAST
#############################################################
for container in containers:
    titleDiv = container.findAll('div', {'class': '_3wU53n'})
    ratingDiv = container.findAll('div', {'class': 'hGSR34'})
    totalRatings = container.findAll('span', {'class': '_38sUEc'})
    price = container.findAll('div', {"class": "_3auQ3N"})
    feature = container.findAll("ul", {"class": "vFw0gD"})
    print("Title: ",titleDiv[0].text)
    print("Ratings: ", ratingDiv[0].text)
    print("Total Ratings: ", totalRatings[0].span.span.text)
    print("Total Reviews:", totalRatings[0].span.contents[2].text)
    print("Price (INR): ", price[0].text.replace("₹", "₹ "))
    nrs = price[0].text.replace("₹", "")
    nrs = nrs.replace(",", "")
    updatedNRS = int(nrs)*1.60
    print("Price (NRS): रू ", "{:,.2f}".format(updatedNRS))
    print("FEATURES OF PRODUCTS: ")
    print('------------------------------------------------')
    for x in (feature):
        for y in x:
            print(y.text)
    print('------------------------------------------------')
    print("\n\n")


