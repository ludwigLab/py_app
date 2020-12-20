################################
#
# File Name: main.py
#
# Date: 18.12.2020
#
# developer: Ludwig Rössler 
#
#################################


##########################
# externel imports  
##########################
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
# Tamplate commands
######################
#
######################


######################
# Build page class
######################
class classLandingPage(GridLayout):
    ########################################################################################
    # function that hold objects "**kwargs" = array unlimit amount of values
    ########################################################################################
    def __init__(self, **objArgs):
        ############################################
        # calls the GridLayout Constructure super = global call
        ############################################
        super(classLandingPage, self).__init__(**objArgs)
        
        ###########################
        # amount of rows from main
        ##########################
        
        self.cols = 1
        
        ############################################
        # create a div to center the submit
        ############################################
        self.divSubmit = GridLayout()
        ###########################
        # amount of rows divSubmit
        ##########################
        self.divSubmit.cols = 2
            
       
        self.divSubmit.add_widget(Label(text="First Name: "))
        self.sclFirstName = TextInput(multiline=False)
        self.divSubmit.add_widget(self.sclFirstName)
        
        self.divSubmit.add_widget(Label(text="Last Name: "))
        self.sclLastName = TextInput(multiline=False)
        self.divSubmit.add_widget(self.sclLastName)
        
        self.divSubmit.add_widget(Label(text="Email: "))
        self.sclEmail = TextInput(multiline=False)
        self.divSubmit.add_widget(self.sclEmail)
        
        #############################
        # add divSubmit to the class
        #############################
        self.add_widget(self.divSubmit)
        
        self.sclSubmit = Button(text="submit", font_size=30)
        ################################################
        # onclick function call funcPressedSubmit
        ################################################
        self.sclSubmit.bind(on_press=self.funcPressedSubmit)
        self.add_widget(self.sclSubmit)
        
    
    def funcPressedSubmit(self, instance):
        ############################################
        # get parameter from input fields
        ############################################
        sclFirstName = self.sclFirstName.text
        sclLastName = self.sclLastName.text
        sclEmail = self.sclEmail.text
        ############################################
        # print test + input parameters
        ############################################
        print("Danke für ihre Anmdelung", sclFirstName, sclLastName)
        print("Ihre Email lautet: ", sclEmail)
        ############################################
        # clear input fields after submit 
        ############################################
        self.sclFirstName.text = ""
        self.sclLastName.text = ""
        self.sclEmail.text = ""
        
##########################
# Master Class
##########################
class classMain(App):
    ######################
    # call appLandingPage
    ######################
    def build(self):
        return classLandingPage()
    
 
 
##########################
# call Master Class 
##########################   
if __name__ == "__main__":
    classMain().run()
    
    
