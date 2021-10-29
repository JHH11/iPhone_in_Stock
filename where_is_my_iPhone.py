import os
import configparser
import time
import requests
from selenium import webdriver




# set path
config_path = '/Users/hau/Documents/Python/iPhone_in_Stock/cfg/config.ini'
chromedriver_path = '/Users/hau/Documents/Python/iPhone_in_Stock/chromedriver'


# read config
config = configparser.ConfigParser()
config.read(config_path)

# LINE TOKEN
line_token = str(config['LINE']['token'])

# describe your iPhone
url = str(config['IPHONE']['url'])
model = str(config['IPHONE']['model'])
color = str(config['IPHONE']['color'])
capacity = str(config['IPHONE']['capacity'])
traid_in = str(config['IPHONE']['traid_in'])

# mapping
model_mapping = eval(config['MAPPING']['model_mapping'])
color_mapping = eval(config['MAPPING']['color_mapping'])
capacity_mapping = eval(config['MAPPING']['capacity_mapping'])
traid_in_mapping = eval(config['MAPPING']['traid_in_mapping'])

# key word about availabiluty
key_word = str(config['AVAILABILITY']['key_word'])


# convert setting for xpath
model_xpath = model_mapping[model]
color_xpath = color_mapping[color]
capacity_xpath = capacity_mapping[capacity]
traid_in_xpath = traid_in_mapping[traid_in]
key_word_xpath = key_word


# launch chrome driver
driver = webdriver.Chrome(executable_path=chromedriver_path)

# navigate url
driver.get(url)
time.sleep(3)

# select model
tmp = "//span[contains(text(), '{}')]".format(model_xpath)
button = driver.find_element_by_xpath(tmp)
button.click()
time.sleep(2)

# select color
tmp = "//span[text()='{}']".format(color_xpath)
button = driver.find_element_by_xpath(tmp)
button.click()
time.sleep(2)

# select capacity
tmp = "//span[text()='{}']".format(capacity_xpath)
button = driver.find_element_by_xpath(tmp)
button.click()
time.sleep(2)

# select train in
tmp = "//span[text()='{}']".format(traid_in_xpath)
button = driver.find_element_by_xpath(tmp)
button.click()
time.sleep(3)


# send a line message if iPhone in stock
try:
    tmp = "//span[contains(text(), '{}')]".format(key_word_xpath)
    driver.find_element_by_xpath(tmp)
    print('有貨')

    def lineNotifyMessage(token, msg):
        headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
        }

        payload = {'message': msg}
        r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
        return r.status_code

    # message
    message = 'iPhone {} {} {} 有貨!!!'.format(model, color, capacity)
    # my private token
    token = line_token

    lineNotifyMessage(token, message)
    print('沒貨')

except:
    print('沒貨')

driver.quit()


