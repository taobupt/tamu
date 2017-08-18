from bs4 import BeautifulSoup


def parse_table(row, tag):
    cols = row.find_all(tag)
    cols = [ele.text.strip() for ele in cols]
    cols=cols[0:8]+cols[9:]
    return cols


def parse_html(location):
    soup = BeautifulSoup(open(location), 'html.parser')
    table=soup.find('table', {'class': 'datadisplaytable'})
    rows = table.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        cols=cols[0:8]+cols[9:]
        data.append(cols)
    data = [x for x in data if x and len(x) > 3]
    return data

def parse(path):
    soup = BeautifulSoup(open(path),'html.parser')
    error = soup.find('table',{'class':'datadisplaytable'})
    trs=error.find_all('tr')
    print(trs[0])
    print(trs)
    print(error)



print(parse_html("/Users/tao/Desktop/yourCourses_files/SSB.html"))
