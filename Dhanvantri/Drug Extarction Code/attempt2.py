import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from lxml import html
drug_names_list = []
usages_list = []
dosages_list = []
warning_list = []
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
        if 'href' in str(li):
            sub_next_page = li.find('a')['href'] 
            sub_sub_url = f'https://www.drugs.com{sub_next_page}'
            page2=requests.get(sub_sub_url) 
            soup2 = BeautifulSoup(page2.text,'html.parser')
            
            drug_name = soup2.find('ul',{'class':"ddc-list-column-2"})
        
            for link in drug_name.find_all('a'):
                
                drug_url = f'''https://www.drugs.com{link.get('href')}'''
                drug_page = requests.get(drug_url)
                drug_soup = BeautifulSoup(drug_page.text,'html.parser')

                drugs = drug_soup.find('div', class_='contentBox')
    
                drug_title = drugs.find('h1')
                if drug_title:
                    drug_names_list.append(drug_title.text) # drug title ready
                
                else:              
                    drug_names_list.append("No Data")
                
                
                
                uses_element = drug_soup.find('h2', {'id': 'uses'})
                if uses_element:
                    uses_p = uses_element.find_all_next('p', limit=2)
                    uses_str = ''
                    for uses in uses_p:
                        uses_str =uses_str +'\n'+ str(uses.text)
                        usages_list.append(uses_str)  # uses ready
            
                else :
                    usages_list.append("No Data")


                            
                warning_element = drug_soup.find('h2', {'id': 'warnings'})
                if warning_element:
                    warning_p = warning_element.find_all_next('p', limit=2)
                    warn_str = ''
                    for warning in warning_p :
                        warn_str=warn_str + '\n' +str(warning.text)
                        warning_list.append(warn_str) # warning ready
                else:
                    warning_list.append("No Data")

                
                
                dosage_element = drug_soup.find('h2', {'id': 'dosage'})
                if dosage_element:
                    dosage_p = dosage_element.find_all_next('p', limit=2)
                    dosage_str = ''
                    for dosage in dosage_p :
                        dosage_str=dosage_str +'\n' +str(dosage.text)
                        dosages_list.append(dosage_str) # warning ready
                else:
                    dosages_list.append("No Data")
                    
                
                data = {
                            'Drug Name': drug_names_list,
                            'Usage': usages_list,
                            'Dosage': dosages_list,
                            'Warning': warning_list
                        }
                # print(data)
                df = pd.DataFrame(data)
                print(df)
                df.to_excel("attempt2_drug_master_data.xlsx", index=False)