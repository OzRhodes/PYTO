from rubicon.objc import *
import pyto_ui as ui
from math import cos,sin,pi

from PIL import Image

class MyClass(ui.View):
  

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    self.lbl = self.makeLabel()
    self.add_subview(self.lbl)

    
    

    self.btn1 = self.makeBtn()
    self.add_subview(self.btn1)
    
    
  def button_pressed(sender):
      lbl.text="pressed"
      print('Pressed')
    
  def makeBtn(self):
    self.btn1 = ui.Button()
    self.btn1.title = 'TITLE' 
    self.btn1.border_width = 2
    self.btn1.corner_radius = 10
    self.btn1.x =150
    self.btn1.y = 500
    self.btn1.action = self.button_pressed
    return  self.btn1
      
    
    
  def makeLabel(self):
    self.lbl = ui.Label()
    self.lbl.frame = (150,100,100,32)
    self.lbl.text = 'TEST'
    self.lbl.text_color = ui.COLOR_RED
    return self.lbl
    
    
if __name__ == '__main__':
  w, h = 350,600
  f = (0, 0, w, h)
  mc = MyClass()
  mc.frame=f
  mc.background_color = ui.COLOR_WHITE
  ui.show_view(mc,ui.PRESENTATION_MODE_SHEET)
  
  
  '''
   add_gesture_recognizer
 add_subview
 alpha
 appearance
 background_color
 become_first_responder
 border_color
 border_width
 button_items
 center
 center_x
 center_y
 clips_to_bounds
 close
 configure_from_dictionary
 content_mode
 corner_radius
 dictionary_representation
 did_appear
 did_disappear
 first_responder
 flex
 frame
 gesture_recognizers
 height
 hidden
 image
 insert_subview
 insert_subview_above
 insert_subview_below
 layout
 load_from_url
 name
 navigation_bar_hidden
 opaque
 origin
 padding
 pop
 push
 remove_from_superview
 remove_gesture_recognizer
 resign_first_responder
 size
 size_to_fit
 subview_with_name
 subviews
 superview
 tint_color
 title
 user_interaction_enabled
 width
 x
 y
  '''