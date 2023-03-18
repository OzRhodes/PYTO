
import pyto_ui as ui


''' 

Function that will run in a simple GUI and offers a 
method of converting from Fahrenheit to Celsius

will be extended to offer vice versa

'''

class MyClass(ui.View):
  

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    self.tf1 = self.makeTextField(20,100) # make input textfield
    self.add_subview(self.tf1)
    self.lbl1 = self.makeLabel(25,160,"Answer")
    
    self.lbl1.font = ui.Font('Menlo', 25)
    self.add_subview(self.lbl1)
    self.lbl2 = self.makeLabel(45,200,"???")
    self.add_subview(self.lbl2)
    self.btnCalc = self.makeButton(25,350,"Calculate")
    self.add_subview(self.btnCalc)
    
    
    


    
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
      self.label.size = (250,50)
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
      self.button.border_color = ui.COLOR_BLACK
      self.button.border_width = 2
      self.button.action = self.button_pressed
      
      
      return self.button

  def button_pressed(sender):
      inputVal = int(sender.tf1.text)
      
      sender.lbl2.text = str((inputVal-32)/1.8)
      return
  
    
if __name__ == '__main__':
  w, h = 500,700
  f = (0, 0, w, h)
  mc = MyClass()
  mc.frame=f
  mc.background_color = ui.COLOR_WHITE
  ui.show_view(mc,ui.PRESENTATION_MODE_SHEET)
  
'''
def fahrenheit_to_celsius(sender):
    field_view = sender.superview.subview_with_name("input")
    label_view = sender.superview.subview_with_name("label")
    f = float(field_view.text)
    c = (f - 32) / 1.8
    label_view.text = str(c) + " C"
    
# Function that will run when converting from Celsius to Fahrenheit
def celsius_to_fahrenheit(sender):
    field_view = sender.superview.subview_with_name("input")
    label_view = sender.superview.subview_with_name("label")
    c = float(field_view.text)
    f = c * 1.8 + 32
    label_view.text = str(f) + " F"
    


# Button to convert Celsius to Farenheit
button_ctof = ui.Button(title="Convert C to F")
button_ctof.size = (100, 50)
button_ctof.center = (view.width/2, view.height/2-150)
button_ctof.flex = [
    ui.FLEXIBLE_TOP_MARGIN,
    ui.FLEXIBLE_BOTTOM_MARGIN,
    ui.FLEXIBLE_LEFT_MARGIN,
    ui.FLEXIBLE_RIGHT_MARGIN
]
button_ctof.action = celsius_to_fahrenheit
view.add_subview(button_ctof)

# Button to convert Farenheit to Celsius
button_ftoc = ui.Button(title="Convert F to C")
button_ftoc.size = (100, 50)
button_ftoc.center = (view.width/2, view.height/2-100)
button_ftoc.flex = [
    ui.FLEXIBLE_TOP_MARGIN,
    ui.FLEXIBLE_BOTTOM_MARGIN,
    ui.FLEXIBLE_LEFT_MARGIN,
    ui.FLEXIBLE_RIGHT_MARGIN
]
button_ftoc.action = fahrenheit_to_celsius
view.add_subview(button_ftoc)

# Label where result will be displayed
label = ui.Label()
label.text = "Waiting for input..."
label.size = (250, 50)
label.center = (view.width/2, view.height/2-50)
label.flex = [
    ui.FLEXIBLE_TOP_MARGIN,
    ui.FLEXIBLE_BOTTOM_MARGIN,
    ui.FLEXIBLE_LEFT_MARGIN,
    ui.FLEXIBLE_RIGHT_MARGIN
]
label.text_alignment = ui.TEXT_ALIGNMENT_CENTER
label.name = "label"
view.add_subview(label)


'''
