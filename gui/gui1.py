# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 15:12:37 2018

@author: Madhu
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory

class Root(BoxLayout):
    def mainPage(self):
        self.clear_widgets()
        mPage = Factory.MainPage()
        self.add_widget(mPage)
    
    def bpPage(self):
        self.clear_widgets()
        bPage = Factory.BpPage()
        self.add_widget(bPage)
        
    def bpInst(self):
        self.clear_widgets()
        bInst = Factory.BpInst()
        self.add_widget(bInst)

class HealthguiApp(App):
    pass        

if __name__ == '__main__':
    HealthguiApp().run()