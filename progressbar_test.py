#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import kivy
from kivy.config import Config
Config.set("input", "mouse", "mouse, disable_multitouch")
from kivy.app import App
from progressbar import MyProgressBar
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock



class MainScreen(BoxLayout):
    """docstring for MainScreen"""
    def __init__(self):
        super(MainScreen, self).__init__()
        self.my_prbar = MyProgressBar()
        self.orientation = 'vertical'
        self.add_widget(Label(text=''))
        self.add_widget(self.my_prbar)
        self.add_widget(Label(text=''))
        # self.my_prbar.set_spacing(1)
        # self.my_prbar.set_background_color(color='#222aaa')
        # self.my_prbar.set_color('#330033')
        # self.my_prbar.set_max(100)
        # self.my_prbar.set_bar_value_percent(0)
        # self.my_prbar.set_bar_value(4)
        # self.my_prbar.set_border_color('finish', '#444444')
        # self.my_prbar.set_border_color('start', '#aaaaaa')
        #self.my_prbar.set_height(value=23)
        Clock.schedule_interval(self.clock_callback, 1)

    def clock_callback(self, dt):
        self.my_prbar.add_value_percent(.5)
    


class TestApp(App):
    """ App class """
    def build(self):
        return MainScreen()



if __name__ in ('__main__', '__android__'):
    TestApp().run()