from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.chrome.service import Service

web = 'https://www.audible.com/search'
serv = Service(executable_path=binary_path)
driver = webdriver.Chrome(service=serv)

driver.get(web)
assert 'Python' in driver.title