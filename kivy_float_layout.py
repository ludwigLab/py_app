################################
#
# File Name: kivy_login_form.üy
#
# Date: 18.12.2020
#
# developer: Ludwig Rössler
#
# use kivy with FloatLayout 
#
#################################

import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class floatLayoutApp(App):
    def build(self):
        return FloatLayout()
    
    
    
    
    
if __name__ == "__main__":
    floatLayoutApp().run()
