from adafruit_circuitplayground import cp
import time
timer_started = False
max_screen_time = 5    #in seconds

while True:
    light = cp.light
    #if screen is on and timer is off
        #turn on timer
        #take start time

    #if the timer is on
        #if screen is on
            #calculate time elapsed
            #if time elapsed > max screen time
                #blink LEDs, turn on alarm, time's up = true
                #timer off
                #start second timer
        #if screen is off
            #take time when screen is off
            #check time elapsed
            #if time elapsed > 5min ish (if the screen has been off for a while)
                #turn off timer

    #if second timer is on
        #if screen is on
            #turn on LEDs and alarm again
        #if screen is off
            #keep LEDs and alarm off


        
        
        

