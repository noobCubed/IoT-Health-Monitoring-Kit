# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 15:12:37 2018

@author: Madhu
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.factory import Factory
from kivy.clock import Clock
from kivy.properties import NumericProperty

import os
import glob
import time
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

sensor_value = 0

class Root(BoxLayout):
    
    sensor_value_c = NumericProperty(0)
    sensor_value_f = NumericProperty(0)
    
    def mainPage(self):
        self.clear_widgets()
        mPage = Factory.MainPage()
        self.add_widget(mPage)
    
    def bpPage(self):
        self.clear_widgets()
        bPage = Factory.BpPage()
        self.add_widget(bPage)
        
    def tempPage(self):
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
        
        Clock.schedule_once(self.read_temp, 10)            

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
            
        
class HealthguiApp(App):
    pass        

if __name__ == '__main__':
    HealthguiApp().run()