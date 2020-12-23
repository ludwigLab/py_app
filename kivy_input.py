################################
#
# File Name: kivy_input.py
#
# Date: 18.12.2020
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



class Touch(Widget):
    
    btn = ObjectProperty()
    
    def on_touch_down(self, touch):
        print("Mouse down", touch)
        
    def on_touch_move(self, touch):
        print("Mouse move", touch)
        
    def on_touch_up(self, touch):
        print("Mouse up", touch)
    
    
class inputTouchApp(App):
    def build(self):
        return Touch()
    
    
if __name__ == "__main__":
    inputTouchApp().run()
    

