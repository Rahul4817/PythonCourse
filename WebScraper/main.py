from bs4 import BeautifulSoup
import requests

# search=input("search for")
# params={"q":search}
r=requests.get("https://www.google.com/")#,params=params)
soup=BeautifulSoup(r.text,"html.parser")

results=soup.find("ol",{"id":"b_results"})

links=results.find_all("li",{"class":"gsc-row"})
for item in links:
    item_text=item.find("a").text
    item_href=item.find("a").attrs["href"]

    if item_text in item_href:
        print(item_text)
        print(item_href)

# r = requests.get('https://www.youtube.com')
# soup = BeautifulSoup(r.text, 'html.parser')
# results = soup.find_all('div', attrs={'class':'product-item item-template-0 alternative'})
# records = []
# for result in results:
#     name = result.find('div', attrs={'class':'name'}).text # result not results
#     price = result.find('div', attrs={'class':'price'}).text[13:-11]
#     records.append((name, price,))
#
#     print(result)




# r = requests.get('https://www.instagram.com')
# soup = BeautifulSoup(r.text, 'html.parser')
# results = soup.find_all('div', attrs={'class':'product-item item-template-0 alternative'})
# records = []
# for result in results:
#     name = result.find('div', attrs={'class':'name'}).text
#     price = result.find('div', attrs={'class':'price'}).text[13:-11]
#     records.append((name, price,))
#
# print(records)