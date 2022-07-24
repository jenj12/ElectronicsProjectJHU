from adafruit_circuitplayground import cp
import time
timer1_on = False
timer2_on = False
max_screen_time = 5    #in seconds
break_time = 60     #in seconds
def notify():
    cp.pixels.fill((50, 0, 0)) #need to add specific instructions: turn led on, blink, sound

def off():
    cp.pixels.fill((50, 0, 0)) # turn everything off

while True:
    light = cp.light
    threshold = 20

    #if screen is on and timer is off
    if light > threshold and timer1_on == False:
        #turn on timer
        timer1_on = True
        #take start time
        initial_time = time.time()

    #if the timer is on
    if timer1_on == True:
        #if screen is on
        if light >= threshold:
            #calculate time elapsed
            time_elapsed = time.time() - initial_time
            #if time elapsed > max screen time
            if time_elapsed > max_screen_time:
                #blink LEDs, turn on alarm, time's up = true
                notify()
                #timer off
                timer1_on = False
                #start second timer
                timer2_on = True
                
        #if screen is off
        elif light < threshold:
            #take time when screen is off
            time_screen_off = time.time()
            #check time elapsed
            t_elapsed = time.time() - time_screen_off
            #if time elapsed > 5min ish (if the screen has been off for a while)
            if t_elapsed > break_time:
                #turn off timer
                timer2_on == False

    #if second timer is on
    if timer2_on == True:
        #if screen is on
        if light > threshold:
            #turn on LEDs and alarm again
            notify()
        #if screen is off
        else:
            #keep LEDs and alarm off
            off()



