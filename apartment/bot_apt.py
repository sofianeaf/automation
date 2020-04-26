#!/usr/bin/python3.6
# -*- coding: utf-8 -*- 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/home/pi/Desktop/automation/tinder/chromedriver')
        

    def login(self):
        self.driver.get('https://immobilienscout24.de')
    
        
                


bot = TinderBot()
bot.login()