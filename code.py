from adafruit_circuitplayground import cp
import time
timer1_on = False
timer2_on = False
max_screen_time = 1200    #in seconds
break_time = 20     #in seconds
break_started = False
screen_off = False
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
            timer1_on = True
            #take start time
            initial_time = time.time()
            print("timer on")
            print(initial_time)

    if screen_off == True:
        t_elapsed = time.time() - time_screen_off
        if t_elapsed > break_time:
            # print("screen has been off for a while")
            if light >= threshold:
                print("restarting timer")
                initial_time = time.time()
                print(initial_time)
                screen_off = False

    #if the timer is on
    if timer1_on == True:
        #if screen is on
        if light >= threshold:
            screen_off = False
            #calculate time elapsed
            time_elapsed = time.time() - initial_time
            #if time elapsed > max screen time
            if time_elapsed > max_screen_time:
                print("time's up!")
                #timer off
                timer1_on = False
                break_started = True
                print("break started")
        elif light < threshold and screen_off == False:
            screen_off = True
            time_screen_off = time.time()            
        
    if timer2_on == False and break_started == True:   
        if light <= threshold:
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
            time_screen_off = time.time()
        else:
            off()
            t_elapsed = time.time() - time_screen_off
            #if time elapsed > 20 seconds (if the screen has been off for a while)
            if t_elapsed > break_time:
                print("rest over")
                #turn off timer
                timer2_on = False
                break_started = False
                cp.play_tone(440, 0.5)
