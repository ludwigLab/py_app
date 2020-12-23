################################
#
# File Name: kivy_popup.py
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
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder


class Widgets(Widget):
    def btn(self):
        show_popup()
    


kv = Builder.load_file("popupkv.kv")



class P(FloatLayout):
    pass



class myApp(App):
    def build(self):
        return Widgets()
    

def show_popup():
    show = P()
    popupWindow = Popup(title="popup Window", content=show, size_hint=(None,None), size=(400,400))
    popupWindow.open()

    
if __name__ == "__main__":
    myApp().run()
    

