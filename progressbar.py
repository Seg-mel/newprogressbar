#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-



# New ProgressBar widget
#
# This module includes following classes:
#  - MyProgressBar
#  - ProgressLine
#  - BorderLine
# 
# New methods for this ProgressBar:
# 
#    add_value(value=1)
#        Add/subtract value to line bar. 
#        Before setting value, you need to set min and max.
#
#    add_value_percent(value=1)
#        Add/subtract percent value to line bar.
#        Not obligatory set min and max.
#
#    convert_to_percent(value)
#        Convert value to percent
#
#    get_bar_value()
#        Get bar value
#
#    get_max()
#        Get max value
#
#    get_min()
#        Get minimum value
#
#    redraw_widget(*args)
#        Method of redraw this widget
#
#    set_background_color(color)
#        Set background color
#
#    set_bar_value(value)
#        Set bar value
#
#    set_bar_value_percent(value=50)
#        Set bar value
#
#    set_border_color(border, color)
#        Set border color.
#        border = 'start'|'finish'
#        color = hex color
#        Example: set_border_color(border='start', color='#111222')
#
#    set_color(hex_color)
#        Set line color
#
#    set_height(value=16)
#        Set widget height
#
#    set_max(value=100)
#        Set maximum value
#
#    set_min(value=0)
#        Set minimum value
#
#    set_padding(value=0)
#        Set padding
#
#    set_spacing(value=0)
#        Set spacing between progressbar elements

import kivy
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, Line
from kivy.utils import get_color_from_hex



Builder.load_file('./progressbar.kv')



class MyProgressBar(BoxLayout):
    """My custom progressbar class"""

    background_color = '#222222'

    def __init__(self, **kwargs):
        super(MyProgressBar, self).__init__(**kwargs)
        self.line_bar = self.children[1]
        self.start_border = self.children[2]
        self.finish_border = self.children[0]
        self.bind(pos=self.redraw_widget)
        self.bind(size=self.redraw_widget)

    def redraw_widget(self, *args):
        """ Method of redraw this widget """
        with self.canvas.before:
            self.canvas.before.clear()
            Color(*get_color_from_hex(self.background_color))
            Rectangle(pos=(self.x, self.y+1), size=self.size)

    def set_bar_value(self, value):
        """ Set bar value """
        if self.get_min()<=value<=self.get_max():
            self.line_bar.bar_value = value
            self.set_bar_value_percent(self.convert_to_percent(value))
        else:
            print 'ERROR: value < min OR value > max. Try Again.'

    def set_bar_value_percent(self, value=50):
        """ Set bar value """
        if (value >= 0) and (value <= 100):
            self.line_bar.bar_value_percent = value
            self.line_bar.redraw_widget()
        else:
            print "ERROR: value < 0 OR value > 100. Try again."

    def set_min(self, value=0):
        """ Set minimum value """
        if value < self.line_bar.max:
            self.line_bar.min = value
            self.line_bar.redraw_widget()
        else:
            print "ERROR: min > max! Try again."

    def set_max(self, value=100):
        """ Set maximum value """
        if value > self.line_bar.min:
            self.line_bar.max = value
        else:
            print "ERROR: max < min! Try again."

    def set_color(self, hex_color):
        """ Set line color """
        self.line_bar.color = hex_color
        self.line_bar.redraw_widget()

    def set_border_color(self, border, color):
        """
        Set border color.
        border = 'start'|'finish'
        color = hex color
        Example: set_border_color(border='start', color='#111222')
        """
        if border == 'start':
            self.start_border.color = color
            self.start_border.redraw_widget()
        elif border == 'finish':
            self.finish_border.color = color
            self.finish_border.redraw_widget()

    def set_background_color(self, color):
        """ Set background color """
        self.background_color = color
        self.redraw_widget()

    def set_height(self, value=16):
        """ Set widget height """
        self.height = value
        self.start_border.redraw_widget()
        self.finish_border.redraw_widget()
        self.line_bar.redraw_widget()

    def set_padding(self, value=0):
        """ Set padding """
        self.padding = value
        # In order to save bar height we will add two values to height 
        self.set_height(self.height+value*2)

    def set_spacing(self, value=0):
        """ Set spacing between progressbar elements """
        self.spacing = value

    def add_value_percent(self, value=1):
        """ 
        Add/subtract percent value to line bar.
        Not obligatory set min and max.
        """
        percent = self.line_bar.bar_value_percent
        if percent+value <= 0:
            self.line_bar.bar_value_percent = 0
        elif percent+value >= 100:
            self.line_bar.bar_value_percent = 100
        else:
            self.line_bar.bar_value_percent+=value
        self.line_bar.redraw_widget()

    def add_value(self, value=1):
        """ 
        Add/subtract value to line bar. 
        Before setting value, you need to set min and max.
        """
        self.add_value_percent(self.convert_to_percent(value))

    def get_min(self):
        """ Get minimum value """
        return self.line_bar.min

    def get_max(self):
        """ Get max value """
        return self.line_bar.max

    def get_bar_value(self):
        """ Get bar value """
        return  self.line_bar.bar_value

    def convert_to_percent(self, value):
        """ Convert value to percent """
        min = self.line_bar.min
        max = self.line_bar.max
        full_length = max-min
        percent_value = 100*value/float(full_length)
        return percent_value



class ProgressLine(Widget):
    """Percent line class"""

    min = 0
    max = 10
    bar_value = 0
    bar_value_percent = 30
    color = '#565656'

    def __init__(self, **kwargs):
        super(ProgressLine, self).__init__(**kwargs)
        self.bind(pos=self.redraw_widget)
        self.bind(size=self.redraw_widget)

    def redraw_widget(self, *args):
        """ Method of redraw this widget """
        print 'POS_PERCENT:',self.bar_value_percent
        with self.canvas:
            self.canvas.clear()
            line_width = float(self.height)/2+1
            new_y = self.y+line_width
            new_x = self.x+self.width*self.bar_value_percent/100
            Color(*get_color_from_hex(self.color))
            Line(points=[self.x, new_y, new_x, new_y], 
                         width=line_width, cap='none')



class BorderLine(Widget):
    """Border line for progress line"""

    color = '#9a9a9a'

    def __init__(self, **kwargs):
        super(BorderLine, self).__init__(**kwargs)
        self.bind(pos=self.redraw_widget)
        self.bind(size=self.redraw_widget)

    def redraw_widget(self, *args):
        """ Method of redraw this widget """
        with self.canvas:
            self.canvas.clear()
            line_width = float(self.height)/2+1
            new_y = self.y+line_width
            new_x = self.x+4
            Color(*get_color_from_hex(self.color))
            Line(points=[self.x, new_y, new_x, new_y], 
                         width=line_width, cap='none')
        


        