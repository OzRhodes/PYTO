
import pyto_ui as ui


''' 

Function that will run in a simple GUI and offers a 
method of converting from Fahrenheit to Celsius

extended with segment picker
'''

class MyClass(ui.View):
  

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    
    self.selected = 1 # 0 for Fahr 1 for Celc derived from segment selector
    
    
    self.tf1 = self.makeTextField(20,120) # make input textfield
    self.add_subview(self.tf1)
    self.lbl1 = self.makeLabel(20,220,"Answer")
    
    self.lbl1.font = ui.Font('Menlo', 25)
    self.add_subview(self.lbl1)
    self.lbl2 = self.makeLabel(22,260,"???")
    self.add_subview(self.lbl2)
    self.btnCalc = self.makeButton(85,340,"Calculate")
    self.add_subview(self.btnCalc)
    
    self.lbl = self.makeLabel(5,75,"Enter value to convert")
    self.lbl.font = ui.Font('Menlo', 22)
    self.add_subview(self.lbl)
    
    self.segment1 = self.makeSegment(200,126)
    self.add_subview(self.segment1)
    
    


  def makeTextField(self, x = 20, y = 100):
    self.text = ui.TextField()
    self.text.size = (250, 50)
    self.text.x = x
    self.text.y = y
    self.text.text = '100'
    self.text.flex = [
        ui.FLEXIBLE_TOP_MARGIN,
        ui.FLEXIBLE_BOTTOM_MARGIN,
        ui.FLEXIBLE_LEFT_MARGIN,
        ui.FLEXIBLE_RIGHT_MARGIN
    ]
    return self.text
    
    
  def makeLabel(self, x=100, y = 100, text ='add text in func call'):
      self.label = ui.Label()
      self.label.text = "result"
      self.label.size = (350,50)
      self.label.x = x
      self.label.y = y
      self.label.font = ui.Font('Menlo',35)
      self.label.text = text
      self.label.text_color = ui.COLOR_BLUE
      self.label.flex = [
      ui.FLEXIBLE_TOP_MARGIN,
      ui.FLEXIBLE_BOTTOM_MARGIN,
      ui.FLEXIBLE_LEFT_MARGIN,
      ui.FLEXIBLE_RIGHT_MARGIN
      ]
      return self.label
      
      
  def makeButton(self, x = 125, y = 100, text = "add text in func call"):
      self.button = ui.Button()
      self.button.size = (150,50)
      self.button.x = x
      self.button.y = y
      self.button.title = text
      self.button.font = ui.Font('Menlo',25)
      self.button.title_color = ui.COLOR_RED
      self.button.border_color = ui.COLOR_BLACK
      self.button.border_width = 2
      self.button.action = self.button_pressed
      
      
      return self.button

  def button_pressed(sender):
      inputVal = int(sender.tf1.text)
      if sender.selected == 0:
          sender.lbl2.text = '{:.2f}'.format((inputVal-32)/1.8) + ' C'
      if sender.selected == 1:
          sender.lbl2.text = '{:.2f}'.format((inputVal*1.8)+32) + ' F'
      print(sender.lbl2)
      return
  
  def makeSegment(self, x=20,y=100):
      self.segment = ui.SegmentedControl()
      
      self.segment.segments = ["Fahr", "Celc"]
      self.segment.width = 150
      self.segment.x = x
      self.segment.y = y
      self.segment.background_color = ui.COLOR_BLACK
      self.segment.flex = [
        ui.FLEXIBLE_BOTTOM_MARGIN,
        ui.FLEXIBLE_TOP_MARGIN,
        ui.FLEXIBLE_LEFT_MARGIN,
        ui.FLEXIBLE_RIGHT_MARGIN
      ]
      self.segment.action = self.did_select
      return self.segment
    
    
  def did_select(sender):
      sender.selected = (sender.segment1.selected_segment) #0 or 1
      return
      
     
     


if __name__ == '__main__':
  w, h = 500,700
  f = (0, 0, w, h)
  mc = MyClass()
  mc.frame=f
  mc.background_color = ui.COLOR_WHITE
  ui.show_view(mc,ui.PRESENTATION_MODE_SHEET)
  
'''
label = ui.Label()
label.font = ui.Font.font_with_style(ui.FONT_TEXT_STYLE_LARGE_TITLE)
label.frame = (0, 20, view.width, 50)
label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
label.flex = [ui.FLEXIBLE_WIDTH]
view.add_subview(label)

]

def did_select(sender):
    label.text = sender.segments[sender.selected_segment]

segmented_control.action = did_select
view.add_subview(segmented_control)



'''
