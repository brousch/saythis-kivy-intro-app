import kivy
kivy.require('1.5.1')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class SayThis(FloatLayout):
    pass

class SayThisApp(App):
    def build(self):
        return SayThis()

if __name__ == '__main__':
    SayThisApp().run()