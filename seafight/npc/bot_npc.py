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
	with open('/home/sofiane/automation/seafight/npc/log.txt', 'a') as logfile:
		logfile.write(sttime + message + '\n')

class SeafightBot():
	def __init__(self):

		options = webdriver.ChromeOptions()

		options.add_argument("--disable-infobars")
		options.add_argument("start-maximized")
		options.add_argument("--disable-extensions")

		options.add_experimental_option("prefs", {
			#"profile.default_content_setting_values.plugins": 1,
    		#"profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
    		#"profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
    		#"PluginsAllowedForUrls": "https://int12.seafight.com"
			"profile.default_content_setting_values.plugins": 1,
			"profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
			"profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
			"profile.content_settings.exceptions.plugins.*,*.setting": 1,
		    "profile.default_content_setting_values.plugins": 1,
			"PluginsAllowedForUrls": "https://int12.seafight.com/"
		})

		options.add_argument('--disable-features=EnableEphemeralFlashPermission')
		options.add_argument('--disable-infobars')
		options.add_argument("--ppapi-flash-version=32.0.0.101")
		options.add_argument("--ppapi-flash-path=/usr/lib/pepperflashplugin-nonfree/libpepflashplayer.so")

		self.driver = webdriver.Chrome(options=options, executable_path='/home/sofiane/automation/seafight/npc/chromedriver')

        # https://github.com/zalando/zalenium/issues/497

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

		logger('logged-in to: ' + username)
		sleep(2)

		stat_to_play_btn = self.driver.find_element_by_xpath('//*[@id="start-play-btn"]')
		stat_to_play_btn.click()
		sleep(2)

		base_window = self.driver.window_handles[0]
		game_window = self.driver.window_handles[1]

		self.driver.switch_to_window(game_window)
		sleep(5)

		allow_flashplayer_link = self.driver.find_element_by_xpath('//*[@id="noflashcheck"]/a')
		allow_flashplayer_link.click()

	def close(self):

		self.driver.stop_client()
		self.driver.close()



bot = SeafightBot()
bot.login(secrets.username, secrets.password)

sleep(2)
#bot.close()
