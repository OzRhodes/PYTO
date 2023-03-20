
import pyto_ui as ui
from PIL import Image

class MyClass(ui.View):
  

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    self.image1 = self.makeImage()
    self.add_subview(self.image1)
       
    
  def makeImage(self):
    pil = Image.open('pythoniosta.jpg')
    #pil = Image.open(urlopen('https://i.imgur.com/CqdrpEb.jpg')) # needs urllib
    wi,hi = pil.size

    self.frame = (0,0,wi/6,hi/6)
        
    self.iv = ui.ImageView()
    self.iv.name = 'img'
    self.iv.image = pil
    self.iv.frame = self.frame   
    #self._style = style
    #self.effect_view = None    
    return self.iv
    
if __name__ == '__main__':
  w, h = 180,180
  f = (0, 0, w, h)
  mc = MyClass()
  mc.frame=f
  mc.background_color = ui.COLOR_WHITE
  ui.show_view(mc,ui.PRESENTATION_MODE_SHEET)
  
  
  '''
  OTHER USABLE METHODS
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