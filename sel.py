# stupid AI that plays 2048 automatically

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element_by_tag_name('html')

for i in range(100):
    for i in range(5):
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.RIGHT)

    htmlElem.send_keys(Keys.LEFT)
