newprogressbar
==============

New Kivy ProgressBar widget



 This module includes following classes:
  - MyProgressBar
  - ProgressLine
  - BorderLine
 
 New methods for this ProgressBar:
 
    add_value(value=1)
        Add/subtract value to line bar. 
        Before setting value, you need to set min and max.

    add_value_percent(value=1)
        Add/subtract percent value to line bar.
        Not obligatory set min and max.

    convert_to_percent(value)
        Convert value to percent

    get_bar_value()
        Get bar value

    get_max()
        Get max value

    get_min()
        Get minimum value

    redraw_widget(*args)
        Method of redraw this widget

    set_background_color(color)
        Set background color

    set_bar_value(value)
        Set bar value

    set_bar_value_percent(value=50)
        Set bar value

    set_border_color(border, color)
        Set border color.
        border = 'start'|'finish'
        color = hex color
        Example: set_border_color(border='start', color='111222')

    set_color(hex_color)
        Set line color

    set_height(value=16)
        Set widget height

    set_max(value=100)
        Set maximum value

    set_min(value=0)
        Set minimum value

    set_padding(value=0)
        Set padding

    set_spacing(value=0)
        Set spacing between progressbar elements
