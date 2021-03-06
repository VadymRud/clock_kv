import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.text import LabelBase

from time import strftime

class ClockForm(BoxLayout):
    pass
#    pass


class ClockApp(App):
    kv_directory = 'templates'
    sw_started = False
    sw_seconds = 0

    def on_start(self):
        Clock.schedule_interval(self.update, 0)

    def update(self, nap):
        if self.sw_started:
            self.sw_seconds += nap

        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')

        m, s = divmod(self.sw_seconds, 60)
        # self.root.ids.stopwatch.text = ('%02d:%02d.[size=40]%02d[/size]' %
        #                                 (int(m), int(s), int(s * 100 % 100)))

    def start_stop(self):
        self.root.ids.start_stop.text = 'Start' if self.sw_started else 'Stop'
        self.sw_started = not self.sw_started

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False

        self.sw_seconds = 0


if __name__ == '__main__':
    LabelBase.register(name='Roboto', fn_regular='fonts/Roboto-Regular.ttf',
                       fn_bold='fonts/Roboto-Bold.ttf',
                       fn_italic='fonts/Roboto-Italic.ttf')

    ClockApp().run()
