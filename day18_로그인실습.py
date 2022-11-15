from selenium import webdriver


driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://mgr.kgitbank.com/main.it')


id_ = driver.find_element_by_css_selector('#div2 > div > div:nth-child(2) > input')
psswd = driver.find_element_by_css_selector('#div2 > div > div:nth-child(3) > input')
btn = driver.find_element_by_css_selector('#div2 > div > p:nth-child(5) > img')

id_.send_keys('20220429-IT-0233')
psswd.send_keys('Coolsw981231!')
btn.click()


input()




