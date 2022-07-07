# ****************kivyMD GUI **********************************
from kivy import Config
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
Config.write()


class MainWindow(MDScreen):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.cols = 1
        self.layout = MDBoxLayout(
            orientation="vertical"
        )
        self.label = MDTextField(
            multiline=True,
            hint_text="Multi-line text",
            font_size=90,
            halign="center"
        )
        self.button = MDRaisedButton(
            text="BUTTON",
            md_bg_color=[0, 0, 1, 1],
            theme_text_color="Custom",
            text_color=[1, 0, 0, 1],
            font_size="30sp",
            pos_hint={"center_x": .5, "center_y": .5},
        )
        self.button.bind(on_press=self.show_data)
        self.processbar = MDProgressBar(color=[1, 0, 0, 1])
        self.processbar.value = 10
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.processbar)
        self.add_widget(self.layout)

    def show_data(self, x):
        self.processbar.value = int(self.label.text)


class MyApp(MDApp):
    def __init__(self):
        super().__init__()

    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MyApp().run()