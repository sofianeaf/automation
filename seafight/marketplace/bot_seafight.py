#!/usr/bin/python3.5
# -*- coding: utf-8 -*- 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from time import sleep
import datetime
import time

import secrets

def logger(message):
    ts = time.time()
    sttime = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H:%M:%S - ')
    with open('/home/pi/Desktop/automation/seafight/log.txt', 'a') as logfile:
        logfile.write(sttime + message + '\n')

class SeafightBot():
    def __init__(self):
        chrome_options = Options()
        #chrome_options.add_argument("--disable-extensions")
        #chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=chrome_options, executable_path='/home/pi/Desktop/automation/seafight/chromedriver')
        #self.driver = webdriver.Chrome(executable_path='/home/pi/Desktop/automation/seafight/chromedriver')
        

    def login(self, username, password):

        self.driver.get('https://seafight.com')
        sleep(2)

        usr_container = self.driver.find_element_by_xpath('//*[@id="bgcdw_login_form_username"]')
        usr_container.send_keys(username)
        psw_container = self.driver.find_element_by_xpath('//*[@id="bgcdw_login_form_password"]')
        psw_container.send_keys(password)
        sleep(2)

        login_btn = self.driver.find_element_by_xpath('//*[@id="loginForm_default_container"]/div[1]/div/form/fieldset[2]/input[1]')
        login_btn.click()
        sleep(2)
        
        marketplace_btn = self.driver.find_element_by_xpath('//*[@id="MenuMarketplacePic"]/div')
        marketplace_btn.click()
        
        logger('logged in to: ' + username)
        
    def close(self):

        self.driver.stop_client()
        self.driver.close()    
        
    def bet(self, item, amount):
        list_items=[
            ['Kristalle','//*[@id="CURRENCY_4"]'], #0
            ['Ogoun-Amulett','//*[@id="ACTIONITEM_43"]'], #1
            ['Lichtmedallion','//*[@id="ACTIONITEM_38"]'], #2
            ['Heilmunition','//*[@id="AMMUNITION_120"]'], #3
            ['Explosivmunition','//*[@id="AMMUNITION_51"]'], #4
            ['Voodoo-Munition','//*[@id="AMMUNITION_186"]'], #5
            ['Waffenmeister','//*[@id="CREW_95"]'], #6
            ['Eisenharpunen','//*[@id="HARPOON_75"]'], #7
            ['Kette','//*[@id="NONPERISHABLEGOODS_70"]'], #8
            ['Truhenschlüssel','//*[@id="NONPERISHABLEGOODS_77"]'], #9
            ['Kettenhemd','//*[@id="NONPERISHABLEGOODS_65"]'], #10
            ['Enterbeil','//*[@id="NONPERISHABLEGOODS_82"]'], #11
            ['Steinschlosspistole','//*[@id="NONPERISHABLEGOODS_83"]'], #12
            ['Hochsegel','//*[@id="SAIL_50"]'], #13
            ['Heilkanone Stufe 2','//*[@id="WEAPON_121"]'], #14
            ['Galionsfigur: Ran','//*[@id="SHIPEXTENSION_7"]'], #15
            ['Haltholzbalken','//*[@id="SHIPEXTENSION_51"]'] #16
            ]
        sleep(2)

        item_container = self.driver.find_element_by_xpath(list_items[item][1]+'/div[1]/input[1]')
        item_submit_btn = self.driver.find_element_by_xpath(list_items[item][1]+'/div[1]/input[2]')
        scr_down_btn = self.driver.find_element_by_xpath('//*[@id="sfcontent_marketplace_eliteitems_list_vscrollerbaseend"]')
        
        while(True):
            try:
                item_container.send_keys(str(amount))
                break
            except:
                scr_down_btn.click()
                
        sleep(1)
        
        while(True):
            try:
                item_submit_btn.click()
                break
            except:
                scr_down_btn.click()
                
        logger('bet ' + str(amount) + ' on item ' + list_items[item][0])
        sleep(2)
        self.driver.refresh()
        
bot = SeafightBot()
bot.login(secrets.username, secrets.password)
bot.bet(16,145000)
sleep(2)
bot.close()
