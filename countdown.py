global countdown

def countdown():
  import time
  from time import sleep
  print ('Your time begins....')
  sleep(3)
  print ('Now.')
  time_ = float(120)

  while time_ >= 0:
    print('Time Remaining - ', (time_) , end='\r')
    time.sleep(1)
    time_ -= 1
  print("Time's up!!")