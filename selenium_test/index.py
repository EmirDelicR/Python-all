import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://www.google.com/')

search_input = browser.find_element_by_xpath('.//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
time.sleep(2)
search_input.clear()
search_input.send_keys("Python")
search_input.send_keys(Keys.ENTER)

# scroll down / up
time.sleep(2)
html_tag = browser.find_element_by_tag_name('html')
html_tag.send_keys(Keys.END)
time.sleep(1)
html_tag.send_keys(Keys.HOME)
time.sleep(1)

# Get current URL
print(browser.current_url)

# brows back
browser.back()
time.sleep(2)

about_link = browser.find_element_by_xpath('.//*[@id="fsl"]/a[3]')
time.sleep(2)
about_link.click()

time.sleep(2)
nested_link = browser.find_element_by_xpath('/html/body/header/div/nav/ul/li[2]/a')
time.sleep(2)
nested_link.click()

# Refreshing page
time.sleep(2)
browser.refresh()
