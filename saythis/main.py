import kivy
kivy.require('1.5.1')

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from components.ttsspeak import ttsSpeak
from components.initialize import initialize_platform


class SayThis(FloatLayout):
    saywhat_text = ObjectProperty(None)
    sayit_button = ObjectProperty(None)
    
    def show_popup(self, text):
        popup = Popup(title='Test popup', content=Label(text=text),
              auto_dismiss=True)
        popup.open()
    
    def say_something(self, text):
        ttsSpeak(text)


class SayThisApp(App):
    def build(self):
        initialize_platform()
        return SayThis()
    

if __name__ == '__main__':
    SayThisApp().run()
