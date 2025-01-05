# Description: A simple countdown timer that takes in a start and end number and counts down from the start number to the end number.

import time

class countdown :
  def __init__(self , start ,end ,  lapse = 1):
    self.start = start
    self.end = end
    self.count = start
    self.lapse = lapse

  def run(self):
    while self.count > 0 and self.count >= self.end:
      if self.count < self.end:
        return F"countdown is finished! {self.count}"        
      print(self.count)
      self.count -= 1
      time.sleep(self.lapse)
    print("countdown is finished")


if __name__ == "__main__":
  start = int(input("enter start number"))
  end = int(input("enter end number"))
  cd = countdown(start , end)
  cd.run()



