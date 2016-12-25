from bs4 import BeautifulSoup
import requests
import re
from sys import argv

class htmlScraper:
    def getRegex(self,keyword):
        return r""+keyword+""

    def getPageContent(self,url):
        page = requests.get(url)
        pageContent = BeautifulSoup(page.content,'html.parser')
        return pageContent.prettify()

    def getkeywordCount(self,regex,pageContent):
        return len(re.findall(regex, pageContent, re.IGNORECASE))

    def getUrl(self,url,keyword):
            return url + keyword



def scrapPageUsingKeyword(url,keyword):
    url = url + keyword
    scrape = htmlScraper()
    try:
        content = scrape.getPageContent(url)
    except:
        return

    regex = scrape.getRegex(keyword)
    keywordCount = scrape.getkeywordCount(regex,content)
    return keywordCount

def printingResult(keyword,keywordCount):
    if (keywordCount is None):
        print('Some problem here, Please check your internet connection.')
    else:
        print('Result : Count of ' + keyword + ' is ', keywordCount)

def main():
    if(len(argv)<=1):
        print ('Give correct parameters to the pyBot!!! ')
        return
    print ('Please wait pyBot is crawling the page....')

    if(len(argv) == 2):
        keyword = argv[1]
        keywordCount = scrapPageUsingKeyword("http://www.shopping.com/products?KW=", keyword)
        printingResult(keyword,keywordCount)

    if(len(argv) == 3):
        keyword = argv[1]
        pageNumber = argv[2]
        keywordCount = scrapPageUsingKeyword("http://www.shopping.com/products~PG-"+pageNumber+"?KW=",keyword)
        printingResult(keyword,keywordCount)


if __name__ == "__main__":
    main()