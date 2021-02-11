from selenium import webdriver
from selenium.webdriver.common.by import By
import time
wd=webdriver.Chrome(executable_path="D:\selenium browser drivers\chromedriver.exe")
wd.get("https://www.expedia.com/")
flights=wd.find_element_by_xpath("//a[@href='?pwaLob=wizard-flight-pwa']")
flights.click()

Oneway=wd.find_element_by_xpath("//span[contains(text(),'One-way')]")
Oneway.click()

wd.find_element_by_xpath("//body/div[@id='app']/div[@id='app-layer-manager']/div[@id='app-layer-base']/div[2]/div[1]/div[1]/div[4]/div[1]/figure[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
wd.find_element_by_xpath("//input[@data-stid='location-field-leg1-origin-menu-input']").send_keys("mumbai")
wd.find_element_by_xpath('//button[@data-stid="location-field-leg1-origin-result-item-button"]').click()
wd.close()







