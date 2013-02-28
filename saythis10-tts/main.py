import kivy
kivy.require('1.5.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

from kivy.properties import ObjectProperty
from components.ttsspeak import ttsSpeak
from components.initialize import initialize_platform


class SayThis(FloatLayout):
    saywhat_text = ObjectProperty(None)
    sayit_button = ObjectProperty(None)

    def say_something(self, text):
        ttsSpeak(text)

class SayThisApp(App):
    def build(self):
        initialize_platform()
        return SayThis()

if __name__ == '__main__':
    SayThisApp().run()
