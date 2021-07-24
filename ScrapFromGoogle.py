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
urls=["https://www.google.com/search?q=panneau+sens+interdit&client=firefox-b-d&sxsrf=ALeKk025pzjXRs7Hek8zyZLuWWEa6w69pQ:1627141135066&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjQ-OqKhfzxAhUizoUKHSuUD9MQ_AUoAXoECAEQAw&biw=1500&bih=875",
      "https://www.google.com/search?q=rue+sens+interdit&client=firefox-b-d&sxsrf=ALeKk00HeOBG4S7ceMxTtj2revZlakrKzw:1627141152427&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiCx46ThfzxAhUqzIUKHSj4Dt0Q_AUoAXoECAEQAw&biw=1500&bih=875&dpr=2#imgrc=6hTlMzAGZclb6M",
      "https://www.google.com/search?q=rue%20sens%20interdit&tbm=isch&tbs=rimg:CeoU5TMwBmXJYd-Je8y8kfz_1&bih=875&biw=1500&client=firefox-b-d&hl=fr&sa=X&ved=0CAIQrnZqFwoTCKjdvZaF_PECFQAAAAAdAAAAABAR",
      "https://www.google.com/search?q=panneau+vitesse+limite&tbm=isch&ved=2ahUKEwiX1bm6hfzxAhUZ_RoKHZhrCW8Q2-cCegQIABAA&oq=panneau+vitess&gs_lcp=CgNpbWcQARgAMgQIIxAnMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOgQIABBDOggIABCxAxCDAToFCAAQsQM6CggAELEDEIMBEENQpJAFWIShBWC0pgVoAHAAeACAAUmIAZEGkgECMTSYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=cjT8YJfUN5n6a5jXpfgG&bih=875&biw=1500&client=firefox-b-d&hl=fr",
      "https://www.google.com/search?q=panneau+vitesse+30+france&tbm=isch&ved=2ahUKEwihtu76hfzxAhVO04UKHUH1ARYQ2-cCegQIABAA&oq=panneau+vitesse+30+france&gs_lcp=CgNpbWcQAzoCCAA6BAgAEB46BggAEAgQHlC-3wRYhucEYMznBGgAcAB4AIABPogB4gKSAQE3mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=-TT8YOHVPM6mlwTB6oewAQ&bih=875&biw=1500&client=firefox-b-d",
      "https://www.google.com/search?q=panneau%20vitesse%20limite&tbm=isch&hl=fr&tbs=rimg:CecAvk3_1J1joYQNigQVLS1QC&client=firefox-b-d&sa=X&ved=0CAIQrnZqFwoTCMiwko6G_PECFQAAAAAdAAAAABAR&biw=1483&bih=875",
      "https://www.google.com/search?q=panneau+routier&tbm=isch&ved=2ahUKEwip6ae6hvzxAhUS_xoKHYhZCeQQ2-cCegQIABAA&oq=panneau+routier&gs_lcp=CgNpbWcQAzIECCMQJzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoECAAQAzoICAAQsQMQgwFQ3KYFWOyqBWDWsgVoAHAAeACAAUaIAYsDkgEBN5gBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=fzX8YOmtA5L-a4izpaAO&bih=875&biw=1483&client=firefox-b-d&hl=fr",
      "https://www.google.com/search?q=panneau%20routier%20france&tbm=isch&hl=fr&tbs=rimg:Ca2AC8-e7tH2YQhwBRMBXg-g&client=firefox-b-d&sa=X&ved=0CAIQrnZqFwoTCIjTk_KG_PECFQAAAAAdAAAAABAR&biw=1483&bih=875",
      "https://www.google.com/search?q=panneau%20routier&tbm=isch&hl=fr&tbs=rimg:CT-X3SgD3E02YX6998OjlT0x&bih=875&biw=1483&client=firefox-b-d&sa=X&ved=0CAIQrnZqFwoTCLCP2eqG_PECFQAAAAAdAAAAABAK",
      "https://www.google.com/search?q=panneau%20routier&tbm=isch&hl=fr&tbs=rimg:Ce9rKcbz38FMYcxOr6OkrAWA&client=firefox-b-d&sa=X&ved=0CAIQrnZqFwoTCMi4wbKH_PECFQAAAAAdAAAAABAI&biw=1483&bih=875",
      "https://www.google.com/search?q=panneau%20routier%20france&tbm=isch&hl=fr&tbs=rimg:CTGd5FAcjLLZYQHZuK97X0sf&bih=875&biw=1483&client=firefox-b-d&sa=X&ved=0CAIQrnZqFwoTCOjb7L-H_PECFQAAAAAdAAAAABAP"]


labels=['s_interdit','s_interdit','s_interdit',"vit_lim","vit_lim","vit_lim","other","other","other","other","other"]
num_images=[100,100,100,100,100,100,100,100,100,100,100]

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
