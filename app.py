from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # Enable dark mode
        return Builder.load_file('app.kv')

MainApp().run()