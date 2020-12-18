################################
#
# File Name: main.py
#
# Date: 18.12.2020
#
# developer: Ludwig Rössler 
#
#################################

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.testinput import Textinput


class MyApp(App):
    def build(self):
        return Label(text="test 1")
    
if __name__ == "__main__":
    MyApp().run()
    
    
