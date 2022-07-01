# ****************kivy GUI **********************************
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.videoplayer import VideoPlayer


class MainWindow(GridLayout):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.cols = 1
        self.video = VideoPlayer(source="kk.mp4")
        self.video.options = {"eos": "loop"}
        self.video.allow_fullscreen = True
        # self.video.allow_stretch = True

        button = Button(text="Play",
                        font_size=50,
                        size_hint_y=None,
                        height=100
                        )
        button.bind(on_press=self.show_video)

        self.add_widget(self.video)
        self.add_widget(button)

    def show_video(self, x):
        self.video.state = "play"


class MyApp(App):
    def __init__(self):
        super().__init__()

    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MyApp().run()