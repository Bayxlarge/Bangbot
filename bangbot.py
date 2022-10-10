#bangbot by bang
import requests
import os
import json
import keyboard 
import socketio 
import threading
import math
import random
import time
import urllib.request
import pyautogui
import math
import PIL
import numpy as np
import itertools
from itertools import cycle
from numpy import sqrt
from PIL import Image, ImageGrab, ImageDraw, ImageFont
from ast import literal_eval as make_tuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sio = socketio.Client()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--disable-webgl")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)



#///////////////////////// this is speed 
speed = 0.02
#///////////////////////// Lower value means speed bot.
class Bang_Bot():
    def __init__(self):
        self.chart = 7 #the map
        self.get_chart()

        self.authkey = None
        self.authtoken = None
        self.authid = None
        self.initial_login()

        self.key = 'f9'
        self.hotkeys()

        self.socket_connection()

    def get_color_index(self):
        try:
            cid = str(driver.find_element(By.XPATH,'/html/body/div[3]/div[2]').get_attribute("style"))
            a = cid.find('(')
            b = cid.find(')');b+=1
            cid = cid[a:b]
        finally:
            return colors.index(make_tuple(cid))


    
    def get_coord(self):
        try:
            self.x, self.y = make_tuple(driver.find_element(By.XPATH,'/html/body/div[3]/div[4]').text)
            return self.x, self.y
            self.x, self.y = self.xy
        except:
             pass
            
    def hotkeys(self): #add more hotkeys in this section
        keyboard.add_hotkey('shift+w', lambda: self.zone('top left'))
        keyboard.add_hotkey('shift+d', lambda: self.zone('bottom right')) 
        keyboard.add_hotkey('w', lambda: self.sus())
        keyboard.add_hotkey('z', lambda: self.tv()) 
        keyboard.add_hotkey('x', lambda: self.bomb())
        keyboard.add_hotkey('a', lambda: self.fill())
        keyboard.add_hotkey('p', lambda: self.protect())#Protecting selected pixels
        keyboard.add_hotkey('d', lambda: self.dotting())
  
      
    def dotting (self):
        color = self.get_color_index()
        x1, y1 = self.get_coord()
        while keyboard.is_pressed('d'):
             pass
        x2, y2 = self.get_coord()
        while True:
            x = random.randint(x1 , x2)
            y = random.randint(y1 , y2)
            if self.cache[x,y] not in [0,0,0] + [(204,204,204)]:
                sio.emit("p",[x,y,color,1])
                time.sleep(speed)
                
            if keyboard.is_pressed('q'):
             print("Cancelled.")
             return
            
            
        
        


    def protect(self):
     color = self.get_color_index()
     x, y = self.get_coord()    
     pixel_list = []
     pixel_list += [[x, y, color],]    
     while True:              
         for pixel in pixel_list:
             if keyboard.is_pressed('q'):
                 print("Cancelled.")
                 return
             if keyboard.is_pressed('p'):
                 color = self.get_color_index()
                 x, y = self.get_coord()
                 pixel_list += [[x, y, color],]
                 time.sleep(speed) 
             if self.cache[pixel[0],pixel[1]] not in [colors[color]] + [(204,204,204)]:
                 sio.emit("p",[pixel[0] , pixel[1] , pixel[2] , 1])
                 time.sleep(speed)
            
        
    
    def fill(self):
        try:
            color = self.get_color_index()
            x1, y1 = self.get_coord()
            while keyboard.is_pressed('a'):
                pass
            x2, y2 = self.get_coord()
            while True:
             if keyboard.is_pressed('q'):
                print("Cancelled.")
                time.sleep(1)
                return
             for x in range (x1, x2 + 1):
                for y in range (y1, y2 + 1): 
                    if self.cache[x,y] not in [colors[color]] + [(204,204,204)]:    
                        sio.emit("p",[x,y,color, 1])
                        time.sleep(speed)
        except Exception as e:
          print(e)
          pass
   
    
    def bomb(self):
        self.get_coord()
        color = self.get_color_index()
        for x in range(7):
            for y in range(7):
                sio.emit("p",[self.x + x, self.y +y, color, 1])
        time.sleep (1)
                

    def tv(self):
        self.get_coord()
        size = int(input("Enter Tv size:  ")) 
        print ("Start TV  press q to stop.")
        while True:
             if keyboard.is_pressed('q'):
                print("Cancelled.")
                time.sleep(1)
                return
             sio.emit("p",[self.x + random.randint(0 , size), self.y + random.randint(0 , size), random.randint(0 , 38), 1])
             time.sleep(speed)
           
    def sus(self):
        self.get_coord()
        suscolor = random.randint(0, 38)
        sio.emit("p",[self.x, self.y, suscolor, 1])
        sio.emit("p",[self.x - 1, self.y, suscolor, 1])
        sio.emit("p",[self.x - 2, self.y, suscolor, 1])
        sio.emit("p",[self.x - 2, self.y + 1, suscolor, 1])
        sio.emit("p",[self.x - 2, self.y + 2, suscolor, 1])
        sio.emit("p",[self.x - 1, self.y + 2, suscolor, 1])
        sio.emit("p",[self.x, self.y + 2, suscolor, 1])
        sio.emit("p",[self.x - 3, self.y + 1, suscolor, 1])
        sio.emit("p",[self.x - 3, self.y + 2, suscolor, 1])
        sio.emit("p",[self.x , self.y + 3, suscolor, 1])
        sio.emit("p",[self.x - 1, self.y + 3, suscolor, 1])
        sio.emit("p",[self.x - 2, self.y + 3, suscolor, 1])
        sio.emit("p",[self.x , self.y + 4, suscolor, 1])
        sio.emit("p",[self.x - 2, self.y + 4, suscolor, 1])
        sio.emit("p",[self.x, self.y + 1, 0, 1])
        sio.emit("p",[self.x - 1, self.y + 1, 0, 1])
    

    
    
    def zone(self, hotkey): #zone constructor
        try:
            self.get_coord()
            if hotkey == 'top left': #top left
                self.txty = self.x, self.y, (pyautogui.position())
                print (f'Top-left marked: {self.txty}')
                try:
                    if self.bxby[0] > self.txty[0] and self.bxby[1] > self.txty[1]:
                        print ('Zone commands ready.')
                        self.zone_commands = True
                except:
                    pass
            if hotkey == 'bottom right': #bottom right
                self.bxby = self.x + 1, self.y + 1, (pyautogui.position())
                print (f'Bottom-right marked: {self.bxby}')
                try:
                    if self.bxby[0] > self.txty[0] and self.bxby[1] > self.txty[1]:
                        print ('Zone commands ready.')
                        self.zone_commands = True
                except:
                    pass
        except:
            pass
    
    
    def emitsleep(self, x, y, color, filters):
        try:
            if self.cache[x,y] not in [colors[color]] + filters + null + self.colorfilter: 
                sio.emit('p',[x, y, color, 1])
                time.sleep(speed - (self.start - time.time()))
                self.start = time.time()
                return True
            else:
                return False
        except:
            return False


    def initial_login(self):
        print (' Welcome to bangbot')
        time.sleep(2)
        print (' Pixelplace is opening...')
        driver.get("https://pixelplace.io")
        while self.authkey == None or self.authtoken == None or self.authid == None:
            try:
                self.authkey = driver.get_cookie("authKey").get('value')
                self.authtoken = driver.get_cookie("authToken").get('value')
                self.authid = driver.get_cookie("authId").get('value')    
                print('Logged in.')
            except:
                print('Please log in.')
                time.sleep(5)
                pass
          
    def socket_connection(self):
        sio.connect('https://pixelplace.io', transports=['websocket'])
        @sio.event
        def connect():
            sio.emit("init",{"authKey":f"{self.authkey}","authToken":f"{self.authtoken}","authId":f"{self.authid}","boardId":self.chart})
            threading.Timer(15, connect).start()
          
        
    def get_chart(self):
        with open(f'{self.chart}.png', 'wb') as f:
            f.write(requests.get(f'https://pixelplace.io/canvas/{self.chart}.png?t={random.randint(999,9999)}').content)
        image = PIL.Image.open(f'{self.chart}.png').convert('RGB')
        self.cache = image.load()    

colors =[(255,255,255),(196,196,196),(136,136,136),(85,85,85),(34,34,34),
        (0,0,0),(0,102,0),(34,177,76),(2,190,1),(81,225,25),(148,224,68),
        (251,255,91),(229,217,0),(230,190,12),(229,149,0),(160,106,66),
        (153,83,13),(99,60,31),(107,0,0),(159,0,0),(229,0,0),(255,57,4),
        (187,79,0),(255,117,95),(255,196,159),(255,223,204),(255,167,209),
        (207,110,228),(236,8,236),(130,0,128),(81,0,255),(2,7,99),(0,0,234),
        (4,75,255),(101,131,207),(54,186,255),(0,131,199),(0,211,221),(69,255,200)]
bangbot = Bang_Bot()
