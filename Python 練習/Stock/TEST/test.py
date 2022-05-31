import requests
from bs4 import BeautifulSoup

def main():
    resp = requests.get('http://jwlin.github.io/py-scraping-analysis-book/ch2/table/table.html')
    soup = BeautifulSoup(resp.text, 'html.parser')
   
    rows = soup.find('table', 'table').tbody.find_all('tr')
    for row in rows:
        all_tds = row.find_all('td') 
        if 'href' in all_tds[3].a.attrs:
            href = all_tds[3].a['href']
        else:
            href = None
        print(all_tds[0].text, all_tds[1].text, all_tds[2].text, href, all_tds[3].a.img['src'])

if __name__ == '__main__':
    main()