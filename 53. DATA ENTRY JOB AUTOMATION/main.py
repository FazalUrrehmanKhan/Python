from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time

form_URL = "https://docs.google.com/forms/d/e/1FAIpQLSftxW_AlRa_tGhlE5Pd8W62sCXJ9ezEBL-B7v5lnLOkIcaw8A/viewform?usp=sf_link"
website_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(website_URL)
soup = BeautifulSoup(response.text, "html.parser")

prices_list = [t.getText().replace("/mo", "").split("+")[0] for t in soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")]
addresses_list = [t.getText().strip() for t in soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")]
links_list = [t.get("href") for t in soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(form_URL)

for i in range(0, len(prices_list)):
    (driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(addresses_list[i]))
    (driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(prices_list[i]))
    driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(links_list[i])
    driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
    time.sleep(1)
    driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
    time.sleep(1)

driver.quit()
