################################
#
# File Name: kivy_graphic.py
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
from kivy.graphics import Rectangle
from kivy.graphics import Color, Line


class createGraphic(Widget):
    def __init__(self, **kwargs):
        super(createGraphic, self).__init__(**kwargs)
        
        with self.canvas:
            Line(points=(20,30,400,500,60,500))
            Color(1,0,0, .5, mode='rgba')
            
            self.rect = Rectangle(pos=(0,0), size=(50,50))
            #Color(1,1,1, .5, mode='rgba') 
            #self.rect = Rectangle(pos=(0,300), size=(150,100))

    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        print("Mouse down")
    
    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print("Mouse move")
    
    

class MyApp(App):
    def build(self):
        return createGraphic()
    


if __name__ == "__main__":
    MyApp().run()