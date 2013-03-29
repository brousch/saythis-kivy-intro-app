import kivy
kivy.require('1.5.1')

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

from components.initialize import initialize_platform
from components.ttsspeak import ttsSpeak


class SayThis(FloatLayout):
    saywhat_text = ObjectProperty(None)

    def say_something(self, text):
        ttsSpeak(text)

    def clear(self):
        self.saywhat_text.text = ""
        self.saywhat_text.focus = True


class SayThisApp(App):
    def build(self):
        initialize_platform()
        return SayThis()
    

if __name__ == '__main__':
    SayThisApp().run()
