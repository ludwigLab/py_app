################################
#
# File Name: kivy_login_form.üy
#
# Date: 18.12.2020
#
# developer: Ludwig Rössler
#
# how to use kivy with propertie file my.kv
#
#################################

######################
# FloatLayout        #
######################
# Dynmaic plament


##########################
# externel imports  
##########################
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


######################
#
######################


class MyGrid(Widget):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    pass


    def funcButtonClick(self):
        print("Name: ", self.username.text, "Password: " , self.password.text)
        self.username.text = ""
        self.password.text = ""
    

class MyApp(App):
    def build(self):
        return MyGrid()
    

if __name__ == "__main__":
    MyApp().run()
    
    #code





    #code
