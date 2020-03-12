#!/usr/bin/python3.6
# -*- coding: utf-8 -*- 

import urllib.request

def dl_webp(url, file_path, file_name):
	full_path = file_path + file_name + '.webp'
	urllib.request.urlretrieve(url, full_path)

# test ...
#url = input('')
#file_name = input('name')

#dl_img(url, '',file_name)
