import requests
from  bs4 import BeautifulSoup 

headers = {
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'Referer': 'https://desifakes.com/threads/kajal-agarwal-nude-fakes-week-4.17944/',
}

link = input("enter desifakes url:")
pages = int(input("enter number of pages:"))
for i in range(1,pages+1):
    if(i == 1):
        response = requests.get(link, headers=headers)
    else:
        response = requests.get(link+'page-'+str(i), headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser') 
    for item in soup.find_all('img'):
        x =item['src']
        x = str(x)
        
        if "data" not in x:
            if x != "https://pornbb.xyz/images/2021/12/05/White-strip-3.png" and x != "https://pornbb.xyz/images/2021/12/02/desifakes-logo03b827558dcd738e.png":
                print(x)