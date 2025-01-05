# # To create stopwatch
import time

class stopwatch:
  def __init__(self ):
    self.strt = None
    self.ellapased = 0
    self.running = False
  
  def menu(self):
    print("\n")
    print("1. start")
    print("2. stop ")
    print("3. reset")

  def start(self):
    if not self.running:
      self.strt = time.time() - self.ellapased 
      self.running=True
      print("stopwatch is running !")

  def stop(self):
    if self.running : 
      self.ellapased = time.time() - self.strt
      self.running = False
      print(f"Stopwatch stopped! runtime : {self.format_time(self.ellapased)}")

  def reset(self):
    self.strt = None
    self.ellapased = 0
    self .running = False
  
  @staticmethod 
  def format_time(seconds):
    mins, secs = divmod(seconds, 60) #perform division and modulus in a single line 
    return f"{int(mins):02}:{secs:05.2f}"

Stopwatch = stopwatch()

if __name__ == "__main__":
  while True:
    Stopwatch.menu()
    ch = input("Enter your choice ")
    
    if ch == "1":
      Stopwatch.start()
    elif ch=="2":
      Stopwatch.stop()
    elif ch == "3":
      Stopwatch.reset()
    else:
      print("enter the valid choice ")
    
    
