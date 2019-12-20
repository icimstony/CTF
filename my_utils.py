import os
import sys

# Clears screen
def clearScreen():
  if sys.platform.startswith('linux'):
    os.system('clear')
  else:
    os.system('cls')