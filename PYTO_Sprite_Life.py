# based on Conway's game of life
# exploiting Sprite kit elements
# 31 Mar 
# TODO 
# - Add initial form 3x3 life element
# - Add a grid
# - Check life / reproduce /death for each cell - Bture force initially 
# - Check cell in grid
# - refresh grid 





import random
import pyto_ui as ui
from rubicon.objc import *
from Foundation import NSBundle
from mainthread import mainthread

import io

NSBundle.bundleWithPath_('/System/Library/Frameworks/SpriteKit.framework').load()

UIApplication = ObjCClass('UIApplication')
SKView = ObjCClass('SKView')
SKScene = ObjCClass('SKScene')
SKShapeNode = ObjCClass('SKShapeNode')
UIColor = ObjCClass('UIColor')


def get_screen_size():				
  app = UIApplication.sharedApplication.keyWindow
  for window in UIApplication.sharedApplication.windows:
    ws = window.bounds.size.width
    hs = window.bounds.size.height
    #break
  return ws,hs


def create_box(point):
    print(point)
    width = 9
    height = 9
    size = CGSize(width, height)
    node = SKShapeNode.shapeNodeWithRectOfSize_(size)
    node.position = point
    return node


  #create a 3x3 shape
  
def create_life_sprite():
    life_sprite = [[1,0,1],[0,1,0],[1,0,1]]
    
    return life_sprite


# We subclass SKScene
class MyScene(SKScene):

  # needs to create a grid and populate it then 
  #Override update
  @objc_method
  def update_(self, current_time):
    life_sprite = create_life_sprite()
    for y in range(3):
        for x in range(3):
            if life_sprite[x][y]: 
                point = (500+(x*9),500+(y*9))
                node = create_box(point)
                node.fillColor = UIColor.blackColor
                self.addChild_(node)
    
    return

class DemoView(ui.View):
  debug = True

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
  @mainthread
  def did_appear(self):
    # SKView can only be created on a presented view
    # Setup SKView
    screen_size = get_screen_size()
    #FullScreen Display
    sz = CGSize(screen_size[0], screen_size[1])
    rect = CGRect(CGPoint(0, 0), sz)
    skview = SKView.alloc().initWithFrame_(rect)


    self.__py_view__.managed.addSubview(skview)
    self.skview = skview
    scene = MyScene.sceneWithSize_(rect.size)
    scene.backgroundColor = UIColor.whiteColor
    skview.presentScene_(scene)



    
  def did_disappear(self):
    self.skview.paused = True


if __name__ == '__main__':
  view = DemoView()
  view.title = 'SpriteKit'
  
  
  ui.show_view(view,ui.PRESENTATION_MODE_FULLSCREEN)