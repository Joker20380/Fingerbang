from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.button import Button

Window.size = (300, 500)
Window.title = 'FingerBang!'

Builder.load_file('main.kv')


class Start_page(Widget):
    def animate_it(self, widget):
        animate = Animation(size_hint=(1, 1))

        animate += Animation(size_hint=(.7, .7))

        animate.start(widget)


class FingerBangApp(App):
    def build(self):
        return Start_page()

if __name__ == "__main__":
    FingerBangApp().run()
