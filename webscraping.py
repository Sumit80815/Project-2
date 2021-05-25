from bs4 import BeautifulSoup
import requests

url = 'https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
mobiles = soup.find_all('div', class_='_3pLy-c row')
for mobile in mobiles:
    mob_name = mobile.find('div', class_='_4rR01T').text
    price = mobile.find('div', class_='_30jeq3 _1_WHN1').text
    rating = mobile.find('div', class_='_3LWZlK').text
    features = mobile.find('ul', class_='_1xgFaf').text

    print(f'''
    Mobile name : {mob_name}
    Price : {price}
    Rating : {rating}
    Features : {features}
    ''')
    print('')
