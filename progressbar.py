#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-



# New ProgressBar widget

import kivy
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, Line
from kivy.utils import get_color_from_hex
from os.path import join, dirname, abspath



Builder.load_file(join(dirname(abspath(__file__)),'./progressbar.kv'))



class NewProgressBar(BoxLayout):
    """My custom progressbar class"""

    def __init__(self, **kwargs):
        super(NewProgressBar, self).__init__(**kwargs)
        ## Get children
        self.line_bar = self.children[1]
        self.start_border = self.children[2]
        self.finish_border = self.children[0]
        ## Set redraw binds
        self.bind(pos=self.redraw_widget)
        self.bind(size=self.redraw_widget)
        ## Create variables
        self._background_color = '#222222'

    @property
    def min(self):
        """
        The property that sets and 
        returns minimum value.
        type: float
        Example
        """
        return self.line_bar.min

    @min.setter
    def min(self, value):
        if value < self.line_bar.max:
            self.line_bar.min = value
            self.line_bar.redraw_widget()
        else:
            print "ERROR: min > max! Try again."

    @property
    def max(self):
        """
        The property that sets and 
        returns maximum value.
        type: float
        """
        return self.line_bar.max

    @max.setter
    def max(self, value):
        if value > self.line_bar.min:
            self.line_bar.max = value
        else:
            print "ERROR: max < min! Try again."

    @property
    def bar_value(self):
        """
        The property that sets and 
        returns progress bar value.
        type: float
        """
        return  self.line_bar.bar_value

    @bar_value.setter
    def bar_value(self, value):
        if self.min<=value<=self.max:
            self.bar_value_percent = self._convert_to_percent(value)
        else:
            print 'ERROR: value < min OR value > max. Try Again.'

    @property
    def bar_value_percent(self):
        """
        The property that sets and 
        returns progressbar value in percent.
        type: float
        """
        return self.line_bar.bar_value_percent

    @bar_value_percent.setter
    def bar_value_percent(self, value):
        if (value >= 0) and (value <= 100):
            self.line_bar.bar_value = self._convert_to_value(value)
            self.line_bar.bar_value_percent = value
            self.line_bar.redraw_widget()
        else:
            print "ERROR: value < 0 OR value > 100. Try again."

    @property 
    def color(self):
        """
        The property that sets and 
        returns progress bar color.
        type: str (hex color)
        """
        return self.line_bar.color

    @color.setter
    def color(self, hex_color):
        self.line_bar.color = hex_color
        self.line_bar.redraw_widget()

    @property 
    def background_color(self):
        """
        The property that sets and 
        returns progress bar background color.
        type: str (hex color)
        """
        return self._background_color

    @background_color.setter
    def background_color(self, color):
        self._background_color = color
        self.redraw_widget()

    @property 
    def border_color(self):
        """
        The property that sets and 
        returns borders color.
        type: str (hex color)
        """
        return self.start_border.color

    @border_color.setter
    def border_color(self, hex_color):
        self.start_border.color = hex_color
        self.finish_border.color = hex_color
        self.start_border.redraw_widget()
        self.finish_border.redraw_widget()

    @property
    def height_widget(self):
        """
        The property that sets and 
        returns progressbar value.
        type: int
        """
        return self.height

    @height_widget.setter
    def height_widget(self, value):
        self.height = value
        self.start_border.redraw_widget()
        self.finish_border.redraw_widget()
        self.line_bar.redraw_widget()

    @property 
    def padding_widget(self):
        """
        The property that sets and 
        returns progressbar padding value.
        type: int
        """
        return self.padding

    @padding_widget.setter
    def padding_widget(self, value):
        self.padding = value
        # In order to save bar height we will add two values to height 
        self.height_widget = self.height+value*2

    @property 
    def spacing_widget(self):
        """
        The property that sets and 
        returns spacing value between elements.
        type: int
        """
        return self.spacing

    @spacing_widget.setter
    def spacing_widget(self, value):
        self.spacing = value

    def add_value(self, value=1):
        """ 
        Add/subtract value to line bar. 
        Before setting value, you need to set min and max.
        value type: float
        """
        self.add_value_percent(self._convert_to_percent(value))

    def add_value_percent(self, value=1):
        """ 
        Add/subtract percent value to line bar.
        Not obligatory set min and max.
        value type: float
        """
        percent = self.line_bar.bar_value_percent
        if percent+value <= 0:
            self.line_bar.bar_value_percent = 0
            self.line_bar.bar_value = self.min
        elif percent+value >= 100:
            self.line_bar.bar_value_percent = 100
            self.line_bar.bar_value = self.max
        else:
            self.line_bar.bar_value_percent+=value
            self.line_bar.bar_value = self._convert_to_value(
                                                self.line_bar.bar_value_percent)
        self.line_bar.redraw_widget()

    def _convert_to_percent(self, value):
        """ 
        Convert value to percent.
        value type: float
        """
        min = self.line_bar.min
        max = self.line_bar.max
        full_length = max-min
        percent_value = 100*value/float(full_length)
        return percent_value

    def _convert_to_value(self, percent_value):
        """
        Convert percent to value.
        value type: float
        """
        min = self.line_bar.min
        max = self.line_bar.max
        full_length = max-min
        value = float(full_length)*percent_value/100
        return value

    def redraw_widget(self, *args):
        """ Method of redraw this widget """
        with self.canvas.before:
            self.canvas.before.clear()
            Color(*get_color_from_hex(self.background_color))
            Rectangle(pos=(self.x, self.y+1), size=self.size)



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
        


        