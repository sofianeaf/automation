#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/home/sofiane/automation/apartment/chromedriver')

    def enterSearch(self):
        # ---------------------
        # --- IMMO SCOUT 24 ---
        # ---------------------
        sleep(1)
        self.driver.get('https://immobilienscout24.de')

        sleep(1)
        # //*[@id="oss-location"]
        city_in = self.driver.find_element_by_xpath('//*[@id="oss-location"]')
        city_in.send_keys("München")

        sleep(1)
        # //*[@id="oss-price"]
        price_in = self.driver.find_element_by_xpath('//*[@id="oss-price"]')
        price_in.send_keys("1500")

        sleep(1)
        # //*[@id="oss-rooms"]
        # //*[@id="oss-rooms"]/option[4]
        room_in = self.driver.find_element_by_xpath('//*[@id="oss-rooms"]/option[4]')
        room_in.click()

        sleep(1)
        # //*[@id="oss-radius"]/option[6]
        scope_in = self.driver.find_element_by_xpath('//*[@id="oss-radius"]/option[6]')
        scope_in.click()

        sleep(1)
        # //*[@id="oss-form"]/article/div/div[3]/button/span[2]
        submit_in = self.driver.find_element_by_xpath('//*[@id="oss-form"]/article/div/div[3]/button/span[2]')
        submit_in.click()

        # ------------------
        # --- WG-GESUCHT ---
        # ------------------
        sleep(3)
        self.driver.execute_script("window.open('');")
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://www.wg-gesucht.de/")

        sleep(1)
        # //*[@id="autocompinp"]
        city_in = self.driver.find_element_by_xpath('//*[@id="autocompinp"]')
        city_in.send_keys("München")

        sleep(1)
        # //*[@id="categories"]/div[2]/button
        room_in = self.driver.find_element_by_xpath('//*[@id="categories"]/div[2]/button')
        room_in.click()
        # //*[@id="categories"]/div[2]/div/div/ul/li[1]
        # //*[@id="categories"]/div[2]/div/div/ul/li[3]
        sleep(1)
        room_in_sub_0 = self.driver.find_element_by_xpath('//*[@id="categories"]/div[2]/div/div/ul/li[1]')
        room_in_sub_0.click()
        sleep(1)
        room_in_sub_2 = self.driver.find_element_by_xpath('//*[@id="categories"]/div[2]/div/div/ul/li[3]')
        room_in_sub_2.click()

        sleep(1)
        # //*[@id="search_button"]
        submit_in = self.driver.find_element_by_xpath('//*[@id="search_button"]')
        submit_in.click()

    def refreshTabs(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(1)
        self.driver.refresh()

        sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(1)
        self.driver.refresh()


bot = TinderBot()
bot.enterSearch()

while(1):
    sleep(15*60)
    bot.refreshTabs()
