from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image


class MainWindow(GridLayout):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.cols = 1
        self.image = Image(allow_stretch=True, keep_ratio=False)
        button = Button(text="button",
                        font_size=50,
                        size_hint_y=None,
                        height=100)
        button.bind(on_press=self.button_signal)
        self.add_widget(self.image)
        self.add_widget(button)

    def button_signal(self, x):
        self.image.source = "hh.jpg"


class MyApp(App):
    def __init__(self):
        super().__init__()

    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MyApp().run()
