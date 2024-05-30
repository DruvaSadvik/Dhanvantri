from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

drug = 'dolo'
url = 'https://pharmeasy.in'
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
Search_box_click = driver.find_element('xpath','//*[@id="__next"]/main/div[3]/div[1]/div/div[1]/div/div[2]/div/div[1]').click()
Search_box_text = driver.find_element('xpath','//*[@id="topBarInput"]').send_keys(drug)
Search = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/main/div[3]/div[1]/div/div[1]/div/div[2]/div/div[1]/div/div/div[2]/a[1]/div/div'))).click()
product = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/main/div/div/div/div[1]/div[1]/div/div/a/div[1]'))).click()


best_price_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/main/div/div[2]/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[2]')))
best_price = driver.find_element('xpath','//*[@id="__next"]/main/div/div[2]/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[2]').text


uses_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/main/div/div[2]/div[2]/div[5]/div[2]/table/tbody/tr[4]/td[2]')))
uses = driver.find_element('xpath','//*[@id="__next"]/main/div/div[2]/div[2]/div[5]/div[2]/table/tbody/tr[4]/td[2]').text


side_effects_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/main/div/div[2]/div[2]/div[5]/div[2]/table/tbody/tr[5]/td[2]')))
side_effects = driver.find_element('xpath','//*[@id="__next"]/main/div/div[2]/div[2]/div[5]/div[2]/table/tbody/tr[5]/td[2]').text

print(f"Best price:{best_price}\nUses:{uses}\nSide_effects:{side_effects}")