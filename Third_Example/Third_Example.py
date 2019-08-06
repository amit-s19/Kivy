import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.properties import ObjectProperty

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(1,1,1, 0.3, mode='rgba')
            self.rect = Rectangle(pos=(0,0), size = (30,30))


    def on_touch_down(self, touch):
        self.rect.pos = touch.pos
        print("Mouse Pressed: ", touch)

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print("Mouse moved: ", touch)

    def on_touch_up(self, touch):
        print("Mouse released: ", touch)

class MyApp(App):
    def build(self):
        return Touch()


if __name__ == "__main__" :
    MyApp().run()
