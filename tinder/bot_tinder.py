#!/usr/bin/python3.6
# -*- coding: utf-8 -*- 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

import secrets
import dl_img

class TinderBot():
	def __init__(self):
		chrome_options = Options()
		#chrome_options.add_argument("--disable-extensions")
		#chrome_options.add_argument("--disable-gpu")
		chrome_options.add_argument("--disable-notifications")
		chrome_options.add_argument("--no-sandbox")
		self.driver = webdriver.Chrome(options=chrome_options, executable_path='/home/sofiane/automation/tinder/chromedriver')
        

	def login(self, username, password):
		self.driver.get('https://tinder.com')
	
		# try 2nd btn
		sleep(5)
		fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
		fb_btn.click()
		
		base_window = self.driver.window_handles[0]
		try:
			self.driver.switch_to_window(self.driver.window_handles[1])
		except:
			# close pop-up
			sleep(3)
			close_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
			close_btn.click()
			
			sleep(1)
			signup_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[4]/div[1]/button')
			signup_btn.click()
			
			sleep(1)
			more_options_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
			more_options_btn.click()
			
			# try 3rd btn
			sleep(1)
			fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button')
			fb_btn.click()
			
			self.driver.switch_to_window(self.driver.window_handles[1])
			pass
		
		# type in information
		sleep(1)
		email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
		email_in.send_keys(username)
		
		sleep(1)
		pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
		pw_in.send_keys(password)

		login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
		login_btn.click()
		
		self.driver.switch_to_window(base_window)
		
		sleep(2)
		popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
		popup_1.click()

		sleep(2)
		popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
		popup_2.click()
		
	def dl_data(self):
		# open profile
		sleep(1)
		driver.send_keys("UP")
		
		# issue: allow notifications window blocking key entries
		
		# TO DO :
		# -> extract link that contains url to .webp
		
		# <div class="profileCard__slider__img Z(-1)" style="background-image: url(&quot;https://images-ssl.gotinder.com/5e6963b75e9e8001000f6917/640x800_75_cbbba3c8-8ae7-4bce-87fb-8dbecfe4e0e5.webp&quot;); background-position: 50% 50%; background-size: auto 100%;"></div>
		# https://images-ssl.gotinder.com/5e6963b75e9e8001000f6917/640x800_75_cbbba3c8-8ae7-4bce-87fb-8dbecfe4e0e5.webp
		#img = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[1]/span/a[2]/div/div[1]/div/div[1]/div/div/div')
		#print(img)
		
	def terminate(self):
		self.driver.stop_client()
		self.driver.close()
                


bot = TinderBot()
bot.login(secrets.username, secrets.password)
bot.dl_data()


#bot.terminate()


"""          
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
"""
