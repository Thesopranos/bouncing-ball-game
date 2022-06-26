from turtle import back
from webbrowser import BackgroundBrowser
import cv2
import numpy as np
import keyboard

# normal koordinat düzlemi
SIZE_Y = 700
SIZE_X = 500
backgorund = np.ones((SIZE_Y,SIZE_X))
cv2.namedWindow("game", cv2.WINDOW_NORMAL) 

# keyboard.is_pressed("q"):
# genislik = SIZE_X, yükseklik = SIZE_Y
# |                  |
# |                  |
# |                  |
# |                  |    
# |                  |
# |                  |
# |        ---       |  
# |                  |  200 px
class Bar:
  def __init__(self, bar_length = 20):
    self.start_position = [int(SIZE_Y/2 - bar_length/2),int(SIZE_Y/2 + bar_length/2), 195,200]
    
class Ball:
  def __init__(self,speed = 5):
    self.up = 0
    self.rigth = 0
    self.left = 0



while True:
  
  cv2.imshow("game",backgorund)
  
  if cv2.waitKey(30) & 0xFF == ord("q"):
    break

cv2.destroyAllWindows()
