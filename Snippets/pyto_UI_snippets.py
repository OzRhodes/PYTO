from rubicon.objc import *
import pyto_ui as ui
from math import cos,sin,pi

class MyClass(ui.View):
  

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    self.btn1 = self.makeBtn()
    self.lbl = self.makeLabel()

    #self.btn1.action = self.button_pressed
    
    self.add_subview(self.lbl)
    self.add_subview(self.btn1)
    
  def makeBtn(self):
    self.btn1 = ui.Button()
    self.btn1.title = 'TITLE' 
    self.btn1.border_width = 2
    self.btn1.corner_radius = 10
    self.btn1.x =150
    self.btn1.y = 500
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