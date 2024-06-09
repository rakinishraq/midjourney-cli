from kivy.lang import Builder
from kivymd.app import MDApp
import midjourney
import textwrap

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # Enable dark mode
        kv_string = textwrap.dedent("""
        BoxLayout:
            orientation: 'vertical'
            padding: dp(32)
            spacing: dp(32)
            Image:
                size_hint_y: 0.75
                source: 'output/62ffac3d-eda2-4d78-bc0f-d85ee87ded25.png'
                allow_stretch: True
                keep_ratio: True
            MDTextField:
                hint_text: "Imagine"
                size_hint_y: 0.20
                font_size: dp(35)
                mode: "rectangle"
        """)
        return Builder.load_string(kv_string)

MainApp().run()