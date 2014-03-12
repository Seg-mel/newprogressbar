#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import kivy
from kivy.config import Config
Config.set("input", "mouse", "mouse, disable_multitouch")
from kivy.app import App
from progressbar import NewProgressBar
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock



class MainScreen(BoxLayout):
    """docstring for MainScreen"""

    def __init__(self):
        super(MainScreen, self).__init__()
        ## Adding widgets to the layout
        self.my_prbar = NewProgressBar()
        self.orientation = 'vertical'
        self.add_widget(Label(text=''))
        self.add_widget(self.my_prbar)
        self.add_widget(Label(text=''))
        ## Get properties
        print 'MAX:', self.my_prbar.max
        print 'MIN:', self.my_prbar.min
        print 'BAR_VALUE:', self.my_prbar.bar_value
        print 'SPACING:', self.my_prbar.spacing_widget
        print 'HEIGHT:', self.my_prbar.height_widget
        print 'COLOR:', self.my_prbar.color
        print 'BACKGROUND_COLOR:', self.my_prbar.background_color
        print 'BORDER_COLOR:', self.my_prbar.border_color
        ## Set properties
        self.my_prbar.min = 0
        self.my_prbar.max = 10
        self.my_prbar.bar_value = 4
        self.my_prbar.spacing_widget = 4
        self.my_prbar.height_widget = 10
        self.my_prbar.color = '#222aaa'
        self.my_prbar.background_color = '#111888'
        self.my_prbar.border_color = '#444fff'
        ## Start kivy clock
        Clock.schedule_interval(self.clock_callback, 1)

    def clock_callback(self, dt):
        ''' Kivy clock method '''
        self.my_prbar.add_value_percent(.5)
        print self.my_prbar.bar_value
    


class TestApp(App):
    """ App class """
    def build(self):
        return MainScreen()



if __name__ in ('__main__', '__android__'):
    TestApp().run()