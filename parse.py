from bs4 import BeautifulSoup
def parse(path):
    soup = BeautifulSoup(open(path),'html.parser')
    error = soup.find('p',{'class':'alert__title'})
    print(error)

parse("/Users/tao/Desktop/untitled.html")