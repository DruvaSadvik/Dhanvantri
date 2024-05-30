import requests
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd
drug_names = []
usages = []
dosages = []
side_eff1s = []
side_eff2s = []
side_eff3s = []

alphabets = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for alpha in alphabets:
    tummy = 3
    url = f'https://www.rxlist.com/drugs/alpha_{alpha}.htm'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    drugs = soup.find('div', class_='w-full')
    link_tags = drugs.find_all('a')
    dummy = 1
    for link in link_tags:
        print(tummy,dummy)
        href = link.get('href')
        if 'https://www.rxlist.com/' in str(href):
            drug_page = requests.get(href)
            drug_soup = BeautifulSoup(drug_page.text, 'html.parser')
            root = html.fromstring(str(drug_soup))

            try:
                drug_expression = '/html/body/section/div[1]/ul/li[1]/span'
                drug_name = (root.xpath(drug_expression))[0].text_content().strip()
                drug_names.append(drug_name)
            except IndexError:
                print("Got IndexError")
                drug_names.append("")


            try:
                usgae_expression = '//*[@id="apPage"]/div/div[2]/p[1]'
                usage = (root.xpath(usgae_expression))[0].text_content().strip()
                usages.append(usage)
            except IndexError:
                print("Got IndexError")
                usages.append("")


            try:
                dosage_expression = '//*[@id="apPage"]/div/div[2]/p[3]'
                dosage = (root.xpath(dosage_expression))[0].text_content().strip()
                dosages.append(dosage)
            except IndexError:
                print("Got IndexError")
                dosages.append("")
            

            try:
                side_eff1_expression = '//*[@id="apPage"]/div/div[2]/ul[1]/li[1]'
                side_eff1 = (root.xpath(side_eff1_expression))[0].text_content().strip()
                side_eff1s.append(side_eff1)
            except IndexError:
                print("Got IndexError")
                side_eff1s.append("")

            
            try:
                side_eff2_expression = '//*[@id="apPage"]/div/div[2]/ul[1]/li[2]'
                side_eff2 = (root.xpath(side_eff2_expression))[0].text_content().strip()
                side_eff2s.append(side_eff2)
            except IndexError:
                print("Got IndexError")
                side_eff2s.append("")

            
            try:
                side_eff3_expression = '//*[@id="apPage"]/div/div[2]/ul[1]/li[3]'
                side_eff3 = (root.xpath(side_eff3_expression))[0].text_content().strip()
                side_eff3s.append(side_eff3)
            except IndexError:
                print("Got IndexError")
                side_eff3s.append("")


            data = {
            'Drug Name': drug_names,
            'Usage': usages,
            'Dosage': dosages,
            'Side Effect 1': side_eff1s,
            'Side Effect 2': side_eff2s,
            'Side Effect 3': side_eff3s
            }
            
            df = pd.DataFrame(data)
            print(df)
            # df.to_excel('drug_master_data.xlsx', index=False)
        dummy=dummy+1
    tummy=tummy+1



















#     import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import csv
# from lxml import html
# drug_names_list = []
# usages_list = []
# dosages_list = []
# warning_list = []
# url = 'https://www.drugs.com/drug_information.html'
# page=requests.get(url)
# soup = BeautifulSoup(page.text,'html.parser')
# for char in range(ord('A'), ord('Z')+1):  
#     next_page = soup.find('a',{'aria-label':"Browse drugs and medications by letter: "+chr(char)}).get('href')
#     sub_page_url = f'https://www.drugs.com{next_page}'
#     page1=requests.get(sub_page_url) 
#     soup1 = BeautifulSoup(page1.text,'html.parser')
#     sub_sub_page = soup1.find('nav',{'aria-label':"Drug list navigation by first letter"})
#     ul_tag = sub_sub_page.find('ul')
#     tummy= 1
#     for li in ul_tag.find_all('li'):
        
#         sub_next_page = li.find('a').get('href') 
#         sub_sub_url = f'https://www.drugs.com{sub_next_page}'
#         page2=requests.get(sub_sub_url) 
#         soup2 = BeautifulSoup(page2.text,'html.parser')
        
#         drug_name = soup2.find('ul',{'class':"ddc-list-column-2"})
#         dummy = 1
#         for link in drug_name.find_all('a'):
            
#             drug_url = f'''https://www.drugs.com{link.get('href')}'''
#             drug_page = requests.get(drug_url)
#             drug_soup = BeautifulSoup(drug_page.text,'html.parser')

#             drugs = drug_soup.find('div', class_='contentBox')
            
            
#             try:
#                 drug_title = drugs.find('h1')
#                 drug_names_list.append(drug_title.text) # drug title ready
            
#             except TypeError:
#                 print("No drug name")
#                 drug_names_list.append("")
            

#             try:
#                 uses_element = drug_soup.find('h2', {'id': 'uses'})
#                 uses_p = uses_element.find_all_next('p', limit=2)
                # uses_str = ''
                # for uses in uses_p:
                #     uses_str =uses_str +'\n'+ str(uses.text)
                #     usages_list.append(uses_str)  # uses ready
            
#             except TypeError:
#                 print("no use found")
#                 usages_list.append("uses_str")


#             try:            
#                 warning_element = drug_soup.find('h2', {'id': 'warnings'})
#                 warning_p = warning_element.find_all_next('p', limit=2)
#                 warn_str = ''
#                 for warning in warning_p :
#                     warn_str=warn_str + '\n' +str(warning.text)
#                     warning_list.append(warn_str) # warning ready
#             except TypeError:
#                 print("no Waning found")
#                 warning_list.append("")

            
#             try:
#                 dosage_element = drug_soup.find('h2', {'id': 'dosage'})
#                 dosage_p = dosage_element.find_all_next('p', limit=2)
#                 dosage_str = ''
#                 for dosage in dosage_p :
#                     dosage_str=dosage_str +'\n' +str(dosage.text)
#                     dosages_list.append(dosage_str) # warning ready
#             except TypeError:
#                 print("no dosage found")
#                 dosages_list.append("")

#             data = {
#             'Drug Name': drug_names_list,
#             'Usage': usages_list,
#             'Dosage': dosages_list,
#             'Warning': warning_list,
#                     }
            
#             df = pd.DataFrame(data)
#             df.to_excel('attempt2_drug_master_data.xlsx', index=False)
#         print(tummy,dummy)
#         dummy = dummy + 1

#             # except AttributeError:
#             #     print('AttributeError')
#         # except TypeError:
#         #     print('Type Error')
#         tummy = tummy + 1