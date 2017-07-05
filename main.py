import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.text import LabelBase


class ClockForm(BoxLayout):
    pass
#    pass


class ClockApp(App):
    kv_directory = 'templates'


if __name__ == '__main__':
    LabelBase.register(name='Roboto', fn_regular='fonts/Roboto-Regular.ttf',
                       fn_bold='fonts/Roboto-Bold.ttf',
                       fn_italic='fonts/Roboto-Italic.ttf')

    ClockApp().run()
