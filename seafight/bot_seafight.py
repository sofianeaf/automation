from selenium import webdriver
from time import sleep

username = 'na3ne3a'
password = 'raszebbibelkamounia'

driver = webdriver.Chrome(executable_path='/home/pi/Desktop/automation/seafight/chromedriver')

driver.get('https://seafight.com')
sleep(2)

usr_container = driver.find_element_by_xpath('//*[@id="bgcdw_login_form_username"]')
usr_container.send_keys(username)
psw_container = driver.find_element_by_xpath('//*[@id="bgcdw_login_form_password"]')
psw_container.send_keys(password)
sleep(2)

login_btn = driver.find_element_by_xpath('//*[@id="loginForm_default_container"]/div[1]/div/form/fieldset[2]/input[1]')
login_btn.click()
sleep(2)

marketplace_btn = driver.find_element_by_xpath('//*[@id="MenuMarketplacePic"]/div')
marketplace_btn.click()

list_items=[
    '//*[@id="CURRENCY_4"]/div[1]/input[1]',
    '//*[@id="ACTIONITEM_43"]/div[1]/input[1]',
    '//*[@id="ACTIONITEM_38"]/div[1]/input[1]',
    '//*[@id="AMMUNITION_120"]/div[1]/input[1]',
    '//*[@id="AMMUNITION_51"]/div[1]/input[1]',
    '//*[@id="AMMUNITION_186"]/div[1]/input[1]',
    '//*[@id="CREW_95"]/div[1]/input[1]',
    '//*[@id="HARPOON_75"]/div[1]/input[1]',
    '//*[@id="NONPERISHABLEGOODS_70"]/div[1]/input[1]',
    '//*[@id="NONPERISHABLEGOODS_77"]/div[1]/input[1]',
    '//*[@id="NONPERISHABLEGOODS_65"]/div[1]/input[1]',
    '//*[@id="NONPERISHABLEGOODS_82"]/div[1]/input[1]',
    '//*[@id="NONPERISHABLEGOODS_83"]/div[1]/input[1]',
    '//*[@id="SAIL_50"]/div[1]/input[1]',
    '//*[@id="WEAPON_121"]/div[1]/input[1]',
    '//*[@id="SHIPEXTENSION_7"]/div[1]/input[1]',
    '//*[@id="SHIPEXTENSION_51"]/div[1]/input[1]'
    ]
sleep(2)


item_container = driver.find_element_by_xpath(list_items[5])
scr_down_btn = driver.find_element_by_xpath('//*[@id="sfcontent_marketplace_eliteitems_list_vscrollerbaseend"]')
while(True):
    try:
        item_container.send_keys('2')
        break
    except:
        scr_down_btn.click()
        
# same for submission of money

