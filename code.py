from adafruit_circuitplayground import cp
import time
timer_started = False
max_screen_time = 5    #in seconds

while True:
    light = cp.light
    #if screen is on
    if light > 20:  
        #if the timer is off
        if timer_started == False:
            lighton_time = time.time()  #get current time in seconds
            timer_started = True    
            print("timer started")

        #if screen is off, don't start timer

        #if the timer is on
        else:
            time_elapsed = time.time() - lighton_time
            if(time_elapsed>max_screen_time):
                print("You've been staring at the screen for too long! Take a break!")
                #Blinking red LEDs
                #Alarm sound
                #time's up = true
    
    #if screen is off
        #if times's up = true
            #turn off alarm and led
            #start second timer (rest timer)
        #else if timer started = true
            #set screen off time
            #if the screen has been off for (5 min), turn timer off
        #else
            #dont do anything

        
        
        

