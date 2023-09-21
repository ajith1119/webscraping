import requests
from bs4 import BeautifulSoup
import pandas as pd

l=['#','#','#']

data_list = []

for i in l:
    url = 'https://codechef.com/users/'+i

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    titles = soup.find_all('div', class_='rating-number')
    for title in titles:
        data_list.append(title.text)
df = pd.DataFrame(data_list, columns=['Title'])

print(data_list)

df.to_csv('scraped_data.csv', index=False)
