import requests
import csv
from bs4 import BeautifulSoup

# Function to extract the data rows from the table


def extract_data_rows(table):
    data_rows = []
    rows = table.find_all('tr')
    for row in rows[1:]:
        data = [cell.get_text(strip=True) for cell in row.find_all('td')]
        data_rows.append(data)
    return data_rows


url = 'https://bnb.bg/Statistics/StInterbankForexMarket/index.htm'
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', class_='table')

data_rows = extract_data_rows(table)
# Exclude the table header and footer rows
data_rows = data_rows[1:-1]


# Stripping cells in 'обем продадени' to format to int while mapping
for x in range(len(data_rows)):
    clean_string = data_rows[x][7].replace(' ', '')
    data_rows[x][7] = clean_string

# Sorting the data rows in descending order by 'обем продадени'
sorted_data = sorted(data_rows, key=lambda x: int(x[7]), reverse=True)


def is_different(new_data, existing_data):
    if len(new_data) != len(existing_data):
        return True

    for i in range(len(new_data)):
        if new_data[i] != existing_data[i]:
            return True

    return False


try:
    with open('forex_scrape.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        existing_data = list(reader)
except FileNotFoundError:
    pass

if is_different(sorted_data, existing_data):
    # Write the sorted data to a new CSV file
    with open('forex_scrape.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(sorted_data)
        print("New data written to forex_scrape.csv")
else:
    print("No changes in data")