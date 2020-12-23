################################
#
# File Name: kivy_navigation.py
#
# Date: 23.12.2020
#
# developer: Ludwig Rössler
#
# use kivy with touch and mouse input 
#
#################################

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen



class MainWindow(Screen):
    pass
    
class SecondWindow(Screen):
    pass
    
class WindowManager(ScreenManager):
    pass
    

kv = Builder.load_file("Navigation.kv")

class MyMainApp(App):
    def build(self):
        return kv
    

if __name__ == "__main__":
    MyMainApp().run()
