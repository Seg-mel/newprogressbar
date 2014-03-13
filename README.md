New Kivy ProgressBar widget
===========================

Standart widget

<img src="https://raw.github.com/Seg-mel/newprogressbar/master/images/screenshot1.png" width='451px;'/>

Widget with spacing between widget elements

<img src="https://raw.github.com/Seg-mel/newprogressbar/master/images/screenshot2.png" width='451px;'/>

Custom widget

<img src="https://raw.github.com/Seg-mel/newprogressbar/master/images/screenshot3.png" width='451px;'/>

####For example, run and look the file progressbar_test.py

This module includes following classes:
 - NewProgressBar
 - ProgressLine
 - BorderLine
 
Methods defined here:
    
    add_value(value=1)
        Add/subtract value to line bar. 
        Before setting value, you need to set min and max.
        value type: float
    
    add_value_percent(value=1)
        Add/subtract percent value to line bar.
        Not obligatory set min and max.
        value type: float
    
    redraw_widget(*args)
        Method of redraw this widget
    
Data descriptors defined here:
    
    background_color
        The property that sets and 
        returns progress bar background color.
        type: str (hex color)
    
    bar_value
        The property that sets and 
        returns progress bar value.
        type: float
    
    bar_value_percent
        The property that sets and 
        returns progressbar value in percent.
        type: float
    
    border_color
        The property that sets and 
        returns borders color.
        type: str (hex color)
    
    color
        The property that sets and 
        returns progress bar color.
        type: str (hex color)
    
    height_widget
        The property that sets and 
        returns progressbar value.
        type: int
    
    max
        The property that sets and 
        returns maximum value.
        type: float
    
    min
        The property that sets and 
        returns minimum value.
        type: float
        Example
    
    padding_widget
        The property that sets and 
        returns progressbar padding value.
        type: int
    
    spacing_widget
        The property that sets and 
        returns spacing value between elements.
        type: int