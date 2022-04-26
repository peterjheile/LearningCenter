from bs4 import BeautifulSoup  

with open("html practice\WebScraping\MyFirstWebScrape.html") as htmlFile:
    content = htmlFile.read()

    soup = BeautifulSoup(content, "lxml")

    # # print(soup.text)
    # # tags = soup.find('h5')
    # priceTags = soup.find_all('h5')
    # for price in priceTags:
    #     # displays text in the tags
    #     print(price.text)
    # # print(soup.prettify)

    menuCards = soup.find_all('div', class_="card")
    for card in menuCards:
        cardName = card.h5.text
        cardPrice = card.p.text
        print(cardName)
        print(cardPrice)

