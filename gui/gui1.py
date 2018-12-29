# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 15:12:37 2018

@author: Madhu
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.factory import Factory
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty

import os
import glob
import time

import csv
import datetime
import pandas as pd 

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

csvData = [['Timestamp', 'Farenheit']]
userData = [['Username', 'Password']]

class Root(BoxLayout):
    
    try:
        open('users.csv')
    except:    
        with open('users.csv', 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(userData)
    
    sensor_value_f = NumericProperty(0)
    
    rec1time = StringProperty('0')
    rec2time = StringProperty('0')
    rec3time = StringProperty('0')
    rec4time = StringProperty('0')
    rec5time = StringProperty('0')
    rec6time = StringProperty('0')
    rec7time = StringProperty('0')
    rec8time = StringProperty('0')
    rec9time = StringProperty('0')
    rec10time = StringProperty('0')
    rec1fahr = NumericProperty(0)
    rec2fahr = NumericProperty(0)
    rec3fahr = NumericProperty(0)
    rec4fahr = NumericProperty(0)
    rec5fahr = NumericProperty(0)
    rec6fahr = NumericProperty(0)
    rec7fahr = NumericProperty(0)
    rec8fahr = NumericProperty(0)
    rec9fahr = NumericProperty(0)
    rec10fahr = NumericProperty(0)
    
    def loginPage(self):
        self.clear_widgets()
        lPage = Factory.Login()
        self.add_widget(lPage)
    
    def signUpPage(self):
        self.clear_widgets()
        sPage = Factory.SignUp()
        self.add_widget(sPage)
        
    def validate(self, username, password, status):       
        reader = csv.reader(open("users.csv"))
        
        d={}

        for row in reader:
            d[row[0]]=row[1:]
        
        try:
            if((d[username])[0] == password):
                self.mainPage()
            else:
                status.text = "Wrong Password"
        except:
            status.text = "User not found"
            
    
    def signUp(self, name, passw, result):
        reader = csv.reader(open("users.csv"))
        
        d={}

        for row in reader:
            d[row[0]]=row[1:]
            
        try:
            d[name]
            result.text = "Username taken"
        except:    
            with open('users.csv', 'a', newline='') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow([name, passw])
        
            result.text = "Signed Up!"
    
    def mainPage(self):
        self.clear_widgets()
        mPage = Factory.MainPage()
        self.add_widget(mPage)
    
    def bpPage(self):
        self.clear_widgets()
        bPage = Factory.BpPage()
        self.add_widget(bPage)
        
    def tempPage(self):
        try:
            open('tempTest.csv')
        except:    
            with open('tempTest.csv', 'w', newline='') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerows(csvData)
        
        self.clear_widgets()
        tPage = Factory.TempPage()
        self.add_widget(tPage)
        
    def bpInst(self):
        self.clear_widgets()
        bInst = Factory.BpInst()
        self.add_widget(bInst)
        
    def tempInst(self):
        self.clear_widgets()
        tInst = Factory.TempInst()
        self.add_widget(tInst)
        
    def tempMeasure(self):
        self.sensor_value_c = 0
        self.sensor_value_f = 0
        
        self.clear_widgets()
        tMeasure = Factory.TempMeasure()
        self.add_widget(tMeasure)
        
        Clock.schedule_once(self.read_temp, 5)            

    def read_temp_raw(self):
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines
 
    def read_temp(self, dt=0):
        lines = self.read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            self.sensor_value_c = float(temp_string) / 1000.0
            self.sensor_value_f = self.sensor_value_c * 9.0 / 5.0 + 32.0
        
        with open('tempTest.csv', 'a', newline='') as csvFile:
            writer = csv.writer(csvFile)
            now = str(datetime.datetime.now().replace(microsecond=0))
            writer.writerow([now, self.sensor_value_f])
        
    def tempRecords(self):
        self.genRecords()
        
        self.clear_widgets()
        tRec = Factory.TempRecords()
        self.add_widget(tRec) 
        
    def genRecords(self):
        with open('tempTest.csv',"r") as f:
            reader = csv.reader(f,delimiter = ",")
            data = list(reader)
            row_count = len(data)
        
        mdata = pd.read_csv('tempTest.csv',delimiter=',')
        
        if row_count <= 11:
            try:
                self.rec1time = str(mdata.iloc[0][0])
                self.rec1fahr = str(mdata.iloc[0][1])
            except:
                pass
            
            try:
                self.rec2time = str(mdata.iloc[1][0])
                self.rec2fahr = str(mdata.iloc[1][1])
            except:
                pass
            
            try:
                self.rec3time = str(mdata.iloc[2][0])
                self.rec3fahr = str(mdata.iloc[2][1])
            except:
                pass
            
            try:
                self.rec4time = str(mdata.iloc[3][0])
                self.rec4fahr = str(mdata.iloc[3][1])
            except:
                pass
            
            try:
                self.rec5time = str(mdata.iloc[4][0])
                self.rec5fahr = str(mdata.iloc[4][1])
            except:
                pass
            
            try:
                self.rec6time = str(mdata.iloc[5][0])
                self.rec6fahr = str(mdata.iloc[5][1])
            except:
                pass
            
            try:
                self.rec7time = str(mdata.iloc[6][0])
                self.rec7fahr = str(mdata.iloc[6][1])
            except:
                pass
            
            try:
                self.rec8time = str(mdata.iloc[7][0])
                self.rec8fahr = str(mdata.iloc[7][1])
            except:
                pass
            
            try:
                self.rec9time = str(mdata.iloc[8][0])
                self.rec9fahr = str(mdata.iloc[8][1])
            except:
                pass
            
            try:
                self.rec10time = str(mdata.iloc[9][0])
                self.rec10fahr = str(mdata.iloc[9][1])
            except:
                pass
        else:
            
            self.rec1time = str(mdata.iloc[row_count-11][0])
            self.rec1fahr = str(mdata.iloc[row_count-11][1])
            
            self.rec2time = str(mdata.iloc[row_count-10][0])
            self.rec2fahr = str(mdata.iloc[row_count-10][1])
            
            self.rec3time = str(mdata.iloc[row_count-9][0])
            self.rec3fahr = str(mdata.iloc[row_count-9][1])
            
            self.rec4time = str(mdata.iloc[row_count-8][0])
            self.rec4fahr = str(mdata.iloc[row_count-8][1])
            
            self.rec5time = str(mdata.iloc[row_count-7][0])
            self.rec5fahr = str(mdata.iloc[row_count-7][1])
            
            self.rec6time = str(mdata.iloc[row_count-6][0])
            self.rec6fahr = str(mdata.iloc[row_count-6][1])
            
            self.rec7time = str(mdata.iloc[row_count-5][0])
            self.rec7fahr = str(mdata.iloc[row_count-5][1])
            
            self.rec8time = str(mdata.iloc[row_count-4][0])
            self.rec8fahr = str(mdata.iloc[row_count-4][1])
            
            self.rec9time = str(mdata.iloc[row_count-3][0])
            self.rec9fahr = str(mdata.iloc[row_count-3][1])
            
            self.rec10time = str(mdata.iloc[row_count-2][0])
            self.rec10fahr = str(mdata.iloc[row_count-2][1])
            
class HealthguiApp(App):
    pass        

if __name__ == '__main__':
    HealthguiApp().run()