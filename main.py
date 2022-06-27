import cv2
import numpy as np
import keyboard
import sys

# normal koordinat düzlemi
SIZE_Y = 700
SIZE_X = 500
background = np.ones((SIZE_Y,SIZE_X))
clean_background = background.copy()
cv2.namedWindow("game", cv2.WINDOW_NORMAL) 

# keyboard.is_pressed("q"):
# genislik = SIZE_X, yükseklik = SIZE_Y
# |                  |
# |                  |
# |                  |
# | *                |  ball
# |                  |
# |                  |
# |        ---       |  bar
# |                  |  200 px
class Bar:
  def __init__(self, uses_background, bar_length = 70):
    self.bar_length = bar_length
    self.left_side = int(SIZE_Y/2 - bar_length/2)
    self.right_side = int(SIZE_Y/2 + bar_length/2)
    self.start_position = [self.left_side,self.right_side, 495,500]
    self.uses_background = uses_background
    self.up_side = SIZE_Y - 205 # alttan 205 px = 495
    
  def movingBar(self, direction = None):
    
    if direction == "rigth":
      self.start_position[0] += 5
      self.right_side += 5
      
      self.start_position[1] += 5
      self.left_side += 5
      
      if self.right_side >= SIZE_X:
        self.right_side = SIZE_X
        self.left_side = SIZE_X - self.bar_length
        
        self.start_position[0] = self.left_side
        self.start_position[1] = self.right_side
        
    elif direction == "left":
      self.start_position[0] -= 5
      self.right_side -= 5
      
      self.start_position[1] -= 5
      self.left_side -= 5
      
      if self.right_side <= self.bar_length:
        self.right_side = self.bar_length
        self.left_side = 0
        self.start_position[0] = self.left_side
        self.start_position[1] = self.right_side
    
    return self.start_position
  
class Ball:
  
  def __init__(self, uses_background, speed = 5):
    self.uses_background = uses_background
    self.speed_X = speed
    self.speed_Y = speed
    self.up_status = 0
    self.down_status = 0
    self.rigth_status = 0
    self.left_status = 0
    self.position_X = 0
    self.position_Y = 0
    
  def movingBall(self, bar_status):
    self.position_X += self.speed_X
    self.position_Y += self.speed_Y
    self.bar_status = bar_status
    
    if self.position_X <= 0:
        self.left_status = not self.left_status
    
    if self.position_X >= SIZE_X:
        self.rigth_status = not self.rigth_status
        
    if self.position_Y <= 0:
        self.up_status = not self.up_status
     
    if (self.bar_status[0]-5 <= self.position_X <= self.bar_status[1] + 5) and (self.bar_status[2]-5 <= self.position_Y <= self.bar_status[3]+5):
        self.down_status = not self.down_status

    if  self.position_Y > self.bar_status[3]+100:
        sys.exit()
        
    if self.up_status == 1 or self.down_status == 1:
        self.speed_Y = -self.speed_Y
    
    if self.rigth_status == 1 or self.left_status == 1:
        self.speed_X = -self.speed_X
        
    return self.position_X, self.position_Y

bar = Bar(uses_background = background)
ball = Ball(uses_background = background)
bar_status = []
direction = None
while True:
  bar_list = bar.movingBar(direction = direction)
  
  ball_pos_x, ball_pos_y = ball.movingBall(bar_status = bar_list)

  if keyboard.is_pressed('d'):
    direction = "rigth"
  
  elif keyboard.is_pressed('a'):
    direction = "left"
  
  bar_list = bar.movingBar(direction = direction)
  bar_x1 = bar_list[0]
  bar_x2 = bar_list[1]
  bar_y1 = bar_list[2]
  bar_y2 = bar_list[3]
  
  cv2.rectangle(background, (bar_x1, bar_y1), (bar_x2, bar_y2),   (0,0,0), -1)
  cv2.circle(background,(ball_pos_x, ball_pos_y),3,0,-1)
  
  cv2.imshow("game",background)
  
  direction == None
  
  background = clean_background.copy()
  
  if cv2.waitKey(30) & 0xFF == ord("q"):
    break

cv2.destroyAllWindows()
