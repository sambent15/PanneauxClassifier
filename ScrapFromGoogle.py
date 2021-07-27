# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 22:39:01 2021

@author: rapha
"""


from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import urllib.request
import json
import os

import time

driver = webdriver.Firefox()
default_path = r"C:\Users\rapha\Desktop\DeepLearningProjet"


def start(out_folder, cat,max_images=100):
    number_of_scrolls=int((max_images + 0)/ 400 + 1) 
    for _ in range(number_of_scrolls):
        for __ in range(10):
            # Multiple scrolls needed to show all 400 images
            driver.execute_script("window.scrollBy(0, 1000000)")
            time.sleep(0.2)
        # to load next 400 images
        time.sleep(0.2)
        try:
            driver.find_element_by_xpath("//input[@value='Afficher plus de résultats']").click()
            time.sleep(0.5)
        except Exception as e:
            print("Less images found:"+ str(e))
            break
    
    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    _path = os.path.join(default_path, out_folder+"\\"  + cat)
    try:
        os.mkdir(_path)
    except:
        pass
   
    os.chdir(_path)
    count_images = len(images)
    print("Listed %s images"%(count_images))
    time.sleep(0.5)
    count = 0
    label_num=len([name for name in os.listdir(_path) if os.path.isfile(name)])
    for image in images:  
        count += 1
        label_num +=1
        if count>max_images:
            break
        else:
            if not image.get_attribute('src') == "":
                print(str(count))
                try:
                    time.sleep(0.1)
                    image.click()
                    time.sleep(0.1)
                    try:
                        big_image = driver.find_element_by_css_selector("#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div > div.v4dQwb > a > img")             
                        #url = driver.execute_script("return document.querySelector('.d87Otf').parentElement.parentElement.parentElement.querySelector(\"[jsname='HiaYvf']\").src")
                        url = big_image.get_attribute("src")
                        print(url)
                        try:
                            urllib.request.urlretrieve(url,cat +"_"+ str(label_num).zfill(6) +".jpg")
                        except:
                            print("indirme hatası")
                    except:
                        print("javascript hatası")
                except:
                    print("tıklanamadı")
    





search_mode=False

#searching with keywords (search_mode=True)
key_words=['vitesse 30 panneau','panneau vitesse limite']

#using urls (search_mode=False)
urls=["https://www.google.com/search?q=panneau+autoroute&client=firefox-b-d&sxsrf=ALeKk02rHpXpgcNCXKVb6IqfXGHaQb_3gA:1627411463619&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjn1cSR9IPyAhVPPBoKHYb1DjcQ_AUoAXoECAEQAw"]


labels=['other']
num_images=[20]

if search_mode:
    for word,label,max_images in zip(key_words,labels,num_images):
        # if not os.path.exists(os.path.join(default_path,"dataset",label)):
        #     os.makedirs(os.path.join(default_path,"dataset",label))
        url = "https://www.google.co.in/search?q="+word+"&source=lnms&tbm=isch"
        driver.get(url)
        start("dataset", label,max_images)
else:
    for url,label,max_images in zip(urls,labels,num_images):
        # if not os.path.exists(os.path.join(default_path,"dataset",label)):
        #     os.makedirs(os.path.join(default_path,"dataset",label))
        driver.get(url)
        start("dataset", label,max_images)    
