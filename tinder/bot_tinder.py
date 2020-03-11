#!/usr/bin/python3.5
# -*- coding: utf-8 -*- 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

import secrets

#678156

class TinderBot():
    def __init__(self):
        chrome_options = Options()
        #chrome_options.add_argument("--disable-extensions")
        #chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=chrome_options, executable_path='/home/pi/Desktop/automation/tinder/chromedriver')
        

    def login(self, username, password):
        self.driver.get('https://tinder.com')

        sleep(5)


        try:
            moreop_btn = self.driver.find_element_by_xpath('self.driver.find_element_by_xpath')
            moreop_btn.click()
        except:            
            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
            fb_btn.click()
            
            try:
                base_window = self.driver.window_handles[0]
                self.driver.switch_to_window(self.driver.window_handles[1])
                sleep(3)
                
                while(True):
                    try:
                        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
                        email_in.send_keys(username)
                        break
                    except:
                        self.driver.refresh()
                        sleep(3)

                pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
                pw_in.send_keys(password)

                login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
                login_btn.click()
                
                self.driver.switch_to_window(base_window)

                popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
                popup_1.click()

                popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
                popup_2.click()

                
            

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login(secrets.username, secrets.password)