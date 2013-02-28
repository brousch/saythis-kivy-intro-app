import kivy
kivy.require('1.5.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class SayThis(FloatLayout):
    saywhat_text = ObjectProperty(None)
    sayit_button = ObjectProperty(None)

    def say_something(self, text):
        popup = Popup(title='Test Popup', 
                      content=Label(text=text),
                      size_hint=(None,None),
                      size=(200,200),
                      auto_dismiss=True)
        popup.open()

class SayThisApp(App):
    def build(self):
        return SayThis()

if __name__ == '__main__':
    SayThisApp().run()
