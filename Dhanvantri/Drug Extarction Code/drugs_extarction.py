import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
drug_list = []
url = 'https://www.drugs.com/drug_information.html'
page=requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
for char in range(ord('A'), ord('Z')+1):  
    next_page = soup.find('a',{'aria-label':"Browse drugs and medications by letter: "+chr(char)}).get('href')
    sub_page_url = f'https://www.drugs.com{next_page}'
    page1=requests.get(sub_page_url) 
    soup1 = BeautifulSoup(page1.text,'html.parser')
    sub_sub_page = soup1.find('nav',{'aria-label':"Drug list navigation by first letter"})
    ul_tag = sub_sub_page.find('ul')
    for li in ul_tag.find_all('li'):
        try:
            sub_next_page = li.find('a')['href'] 
            sub_sub_url = f'https://www.drugs.com{sub_next_page}'
            page2=requests.get(sub_sub_url) 
            soup2 = BeautifulSoup(page2.text,'html.parser')
            try:
                drug_name = soup2.find('ul',{'class':"ddc-list-column-2"})
                for li1 in drug_name.find_all('li'):
                    drug_list.append(li1.text)
                    
                    print(li1.text)
            except AttributeError:
                continue
        except TypeError:
            continue
with open('D:/Projctzz/Drug_Dealer/drugs.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for drug in drug_list:
        writer.writerow([drug])