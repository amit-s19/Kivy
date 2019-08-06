import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class Widgets(Widget):
    def btn(self):
        show_popup()

class PContent(FloatLayout):
    pass

class MyApp(App):
    def build(self):
        return Widgets()
1

def show_popup():
    p = PContent()
    popupwindow = Popup(title="Popup Window", content=show, size_hint=(None,None), size = (400,400))
    popupwindow.open()


if __name__ == '__main__':
    MyApp().run()
