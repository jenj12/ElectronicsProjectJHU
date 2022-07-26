from adafruit_circuitplayground import cp
import time
timer1_on = False
timer2_on = False
max_screen_time = 10    #in seconds
break_time = 5     #in seconds
break_started = False
def notify():
    cp.pixels.fill((50, 0, 0)) #need to add specific instructions: turn led on, play sound
    cp.play_tone(260, 0.5)
    time.sleep(0.2)

def off():
    cp.pixels.fill((0, 0, 0)) # turn everything off

while True:
    light = cp.light
    threshold = 10

    #if screen is on and timer is off
    if light > threshold:
        if break_started == False and timer1_on == False :
        #turn on timer
            timer1_on = True
            #take start time
            initial_time = time.time()
            print("timer on")
            print(initial_time)

    #if the timer is on
    if timer1_on == True:
        #if screen is on
        if light >= threshold:
            #calculate time elapsed
            time_elapsed = time.time() - initial_time
            #if time elapsed > max screen time
            if time_elapsed > max_screen_time:
                print("time's up!")
                #timer off
                timer1_on = False
                break_started = True
                print("break started")
        
    if timer2_on == False and break_started == True:   
        if light < threshold:
            print("start rest")
            off()
            #start second timer
            timer2_on = True
            time_screen_off = time.time()
            print(time_screen_off)
        else:
            notify()


    #if second timer is on
    if timer2_on == True:
        #if screen is on
        if light > threshold:
            print("go back to rest!")
            #turn on LEDs and alarm again
            notify()
        else:
            off()
            t_elapsed = time.time() - time_screen_off
            #if time elapsed > 5min ish (if the screen has been off for a while)
            if t_elapsed > break_time:
                print("rest over")
                #turn off timer
                timer2_on = False
                break_started = False