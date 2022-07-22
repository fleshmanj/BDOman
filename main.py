import time
import sys
import modes

"""
Write only one statement per line.
Write what you mean, not how to program it
Give proper indentation to show hierarchy and make code understandable.
Make the program as simple as possible.
Conditions and loops must be specified well ie. begun and ended explicity as in given pseudocode examples :
"""



print("starting program")
time.sleep(2)
fisherman = modes.Fishing()
print("starting fishing")
while True:
    fisherman.start_fishing()
    time.sleep(1)
    fisherman.play_minigame()
    time.sleep(5)
