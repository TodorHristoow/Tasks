import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_European_Union_member_states_by_population'
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table', class_='sortable wikitable')
rows = table.find_all('tr')
# Exclude the table header row
rows = rows[1:]

countries_dictionary = {}
for row in rows:
    columns = row.find_all('td')
    country = columns[1].text.strip()
    population = int(columns[2].text.replace(',', '').strip())

    countries_dictionary[country] = {'country_population': population}

EU_population = sum(country_data['country_population'] for country_data in countries_dictionary.values())

for country_data in countries_dictionary.values():
    country_population = country_data['country_population']
    country_population_percentage = (country_population / EU_population) * 100
    country_data['country_population_percentage'] = f'{country_population_percentage:.2f}'

print(countries_dictionary)