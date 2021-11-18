# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:51:01 2021

@author: klkel
"""

import RPi.GPIO as gpio
import time
import spidev
import os
import threading
from datetime import datetime


#initial values
dist=30
pot_per=0
angle=0
stop_run=False
count=0
start_time=0
mode="MS"
filename=''
frequen=2000

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)



#pins used
Red = 5
Green = 6
Blue = 13
LED=14
SW=16
ECHO = 24
trig = 25
buzzer_pin=18

RGB = [Red, Green, Blue]
gpio.setup(RGB, gpio.OUT, initial=gpio.HIGH)
gpio.setup(ECHO, gpio.IN)
gpio.setup(trig, gpio.OUT, initial=gpio.LOW)
gpio.setup(buzzer_pin,gpio.OUT)
gpio.setup(SW, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(LED,gpio.OUT)


rgbfreq = 100
rgbdc = 0
p1 = gpio.PWM(RGB[0], rgbfreq)
p2 = gpio.PWM(RGB[1], rgbfreq)
p3 = gpio.PWM(RGB[2], rgbfreq)
light=gpio.PWM(LED,2)#LED at freq 2
buzzer=gpio.PWM(buzzer_pin,2000) #2 khz freq

p1.start(rgbdc)
p2.start(rgbdc)
p3.start(rgbdc)
light.start(0)
buzzer.start(0)

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)  # open spi port 0, device (CS) 0
spi.max_speed_hz=1000000


pot_channel = 2 # Define sensor channel
delay = 1 # Define delay between readings


# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
    response = spi.xfer2([1,(8+channel)<<4,0])   #1000 0000    Start byte 00000001, channel selection: end byte
    #print(response)
    data = ((response[1]&3) << 8) + response[2]         #011
    #print(data)
    return data
 
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data, places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts, places)
    return volts


# Function to change the RGB LED values
def RGB_LED(R, G, B):
    
    p1.ChangeDutyCycle(R)
    p2.ChangeDutyCycle(G)
    p3.ChangeDutyCycle(B)
    
# Function to decide what RGB LED values to change to	
def ConvertColor(hue):
    saturation=1
    lightness=.5
    r=0
    b=0
    g=0
    C=(100-abs(2*lightness-100))*saturation
    X=C*(1-abs((hue/60)%2-1))
    m=lightness-C/2
    if hue>=360:
        hue=hue-360
    elif hue<0:
        hue=hue+360
        
    if hue>=0 and hue<10: #red
        r=C
        g=X
        b=0
    elif hue>=10 and hue<20:
        r=C
        g=X
        b=0   
    elif hue>=20 and hue<30:
        r=C
        g=X
        b=0
    elif hue>=30 and hue<40: #orange
        r=C
        g=X
        b=0
    elif hue>=40 and hue<60:
        r=C
        g=X
        b=0
    elif hue>=60 and hue<65: #Yellow
        r=C
        g=X
        b=C/16
    elif hue>=65 and hue<80:
        r=C/2+X/2
        g=X/2+C/2
        b=0
    elif hue>=80 and hue<85:
        r=C/4+X*3/4
        g=X/4+C*3/4
        b=0
    elif hue>=85 and hue<100: #green
        r=X
        g=C
        b=0
    elif hue>=100 and hue<130:
        r=X*3/4
        g=C
        b=X/4
    elif hue>=130 and hue<150:
        r=X/4
        g=C
        b=X/2
    elif hue>=150 and hue<160:
        r=X/16
        g=C
        b=X*3/4
    elif hue>=160 and hue<165:
        r=0
        g=C
        b=X*3/4
    elif hue>=165 and hue<170:
        r=0
        g=C
        b=X*13/16
    elif hue>=170 and hue<190: #blue
        r=0
        g=C
        b=X
    elif hue>=190 and hue<240: #blue/indigo
        r=0
        g=X
        b=C
    elif hue>=240 and hue<260:#indigo/violet
        r=X
        g=0
        b=C
    elif hue>=260 and hue<300: #violet
        r=X
        g=0
        b=C
    elif hue>=300 and hue<340:
        r=C*3/4+X/4
        g=0
        b=X/4+C*3/4
    elif hue>=340 and hue<=360:
        r=C
        g=0
        b=C
        
    R=int((r+m)*255)
    G=int((g+m)*255)
    B=int((b+m)*255)
    
    if R>255:
        R=255
    if G>255:
        G=255
    if B>255:
        B=255
    if R<0:
        R=0
    if G<0:
        G=0
    if B<0:
        B=0

    red = 100 - (255-int(R))*100/255 #on a scale of 0-255
    green = 100 - (255-int(G))*100/255
    blue = 100 - (255-int(B))*100/255
    Red=round(red)
    Green=round(green)
    Blue=round(blue)
    RGB_LED(Red,Green,Blue)
    return (Red,Green,Blue)

# Function to have buzzer ring or not
def buzzers():
    while(True):
        
        global stop_run
        if stop_run==True:
            break
        #print('buzzer')
        global frequen
        global mode
        if mode!='ORD':
            
            global dist
            distance=dist
            time.sleep(.15)
            #time.sleep(0.05) #give buzzer some delay
            if distance < 20:      #Check whether the distance is within range
                if distance<4:
                    frequen=2000
                    buzzer.ChangeFrequency(frequen)
                
                    buzzer.ChangeDutyCycle(1)
                    

                    try:
                        time.sleep(.5)
                        
                        buzzer.ChangeDutyCycle(0)
                    except:
                        
                        buzzer.ChangeDutyCycle(0)
                        

                    #DC=0.005 #1Hz/2kHz
                    DC=0
                else: 
                    freq=-118.75*distance+2475 #(4,2000),(20,100)
                    frequen=round(freq)
                    if frequen<=0:
                        frequen=2000
                        DC=0
                    elif frequen<=100:
                        frequen=100
                        DC=1
                    elif frequen>=2000:
                        frequen=2000
                        DC=0
                    else:
                        DC=1
            else:
                frequen=2000
                DC=0 #1Hz/2kHz
        else:
            frequen=2000
            DC=0


        buzzer.ChangeFrequency(frequen)
        buzzer.ChangeDutyCycle(DC)

# Function to get the ultrasonic sensor values and display it to terminal  
def sonic():
    while True:
        #print("Sonic")
        global stop_run
        if stop_run==True:
            break
        try:
            time.sleep(0.1)  # sampling rate
            #sending a pulese to trig pin

            gpio.output(trig, True)
            time.sleep(0.00001)
            gpio.output(trig, False)
            
            while gpio.input(ECHO)==0:               #Check whether the ECHO is LOW
                pulse_start = time.time()              #Saves the last known time of LOW pulse

            while gpio.input(ECHO)==1:               #Check whether the ECHO is HIGH
                pulse_end = time.time()                #Saves the last known time of HIGH pulse 

            pulse_duration = (pulse_end - pulse_start)*1000000 #Get pulse duration to a variable in uS
            #print(pulse_duration)

            distance = pulse_duration / 58.0        #Multiply pulse duration by 17150 to get distance       
            
            global dist
            global pot_per
            time.sleep(0.05)
            dist=round(distance-.5,2) #Round to two decimal points
            if mode=="ORD" or mode=="RDM":
                current_time=datetime.now().strftime("%m/%d/%Y_%H:%M:%S.%f")[:-3] #get date and time down to milliseconds
                data.append({'Time':current_time,'Potentiometer':pot_per,'Distance':(dist)})

            if mode=="MS" or mode=='RDM':
                global frequen
                print("Distance : {} cm, frequency: {} Hz".format((dist),frequen))

                
        except:
            break
        
# Function to get the potentiometer values and display it to terminal
def pot():
    global angle
    while True:
        
        global stop_run
        if stop_run==True:
            break
        try:
            time.sleep(0.5) #sampling rate
            pot_level = ReadChannel(pot_channel)
            pot_volts = ConvertVolts(pot_level, 2)
            pot_angle = (pot_volts*360)/3.3
            
            pot_angle=round(pot_angle,2)
            pot_percent=(pot_angle/360)*100
            pot_percent=round(pot_percent,2)
            global pot_per
            pot_per=pot_percent
            angle=pot_angle
            if mode=="ORD" or mode=="RDM":
                current_time=datetime.now().strftime("%m/%d/%Y_%H:%M:%S.%f")[:-3] #get date and time down to milliseconds
                data.append({'Time':current_time,'Potentiometer':pot_percent,'Distance':(dist)})
            
            if mode=="MS" or mode=="RDM":
                R,G,B=ConvertColor(angle)
                # Print out results
                print("Pot : {} %, RGB: {}".format(pot_percent,[R,G,B]))
            if mode=='ORD':
                RGB_LED(0,0,0) #turn off leds
                
        except:
            
            RGB_LED(0,0,0) #turn off leds
            break


data=[]
current_time=""
header_add=True
beginning=1

#Change LED rate
def changeLedRate(dc):
    light.ChangeDutyCycle(dc)
    time.sleep(0.1)

#change mode based on button press. 1 press=MS, 2 press in 1 sec=RDM, 1 press >2sec= ORD
#due to poor hw, debounce is not the most consistant
def setMode(sw):
    global start_time
    global count
    global beginning
    time_lasted=0
    check_time=0
    time_ended=0
    if beginning==1:
        count=0 #prevent false start
        beginning=0
        
    #gpio.wait_for_edge(SW,gpio.FALLING, timeout=350)
    if count==1:
        st2=time.time()
        if (st2-start_time)>1000:
            start_time=st2
            st2=0
            count=0
            #print(start_time,st2)
        #else:
            #print(start_time,st2)
    else:
        start_time=time.time()
        count=0
        
    
    #time.sleep(.1)
    lasted_long=False
    while gpio.input(sw)==False: #wait for button release
        t_check=time.time()
        if count>0:
            if t_check-st2>2:
                lasted_long=True
                break
        else:
            if t_check-start_time>2: #held longer than  seconds
                
                lasted_long=True
                break
        
    
    time_ended=time.time()
    #print(count)
##    try:
##        time.sleep(.3)
##    except:
##        pass
    global mode
    global filename
    global header_add
    if count<=0:
        time_lasted=time_ended-start_time #no check for rdm
    else:
        time_lasted=time_ended-st2 #check for rdm
        
    if mode=="RDM" or mode=='ORD':
        makeCSV()
        print("stopped recording...",filename)
        header_add=True
    #print(lasted_long)
    if lasted_long==True: #timeout occurred, >2sec
        count=0
        time.sleep(.25) #debounce
        mode="ORD" #change modes
        # print("Ord")
        # print("Led blink")
        changeLedRate(50) #make led blink
            
        filename=datetime.now().strftime("%B_%d_%Y_%H_%M_%S") #get date and time 
        filename=filename+'.csv'
        print("Recording Data....",filename)
        
        lasted_long=False
    elif time_lasted>1:

        count=0
        mode="MS"
        # print("MS")
        # print("LED off")
        gpio.output(LED,gpio.LOW)
        changeLedRate(0)
        time.sleep(.1)
    else:
        tl2=time_ended-start_time
        #print(tl2)
        if tl2<=1 and count==1:
            # print("RDM")
            # print("LED On")
            mode="RDM"
            changeLedRate(100)
            count=0
            time.sleep(.1)
                        
            filename=datetime.now().strftime("%B_%d_%Y_%H_%M_%S") #get date and time 
            filename=filename+'.csv'
            print("Recording Data....",filename)

        else:
            #time.sleep(1) #sleep 1 second to make sure not rdm
            #if count!=0: #rdm changes count to 0
            if tl2>1:
                count=0
                mode="MS"
                #print("MS")
                changeLedRate(0)
                time.sleep(.1)
            else:
                count=count+1
                mode='MS'
                
                changeLedRate(0)

gpio.add_event_detect(SW,gpio.FALLING,callback=setMode,bouncetime=300)
#setMode(SW)

# Function makes or appends to a csv file
def makeCSV():
    import csv
    global filename
    global header_add
    fname="/home/pi/Documents/"+filename
    fieldnames=['Time','Potentiometer','Distance']
    try:
        with open(fname,'a',newline='') as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
            if header_add==True:
                writer.writeheader()
                header_add=False
            writer.writerows(data)
    except:
        with open(fname,'w',newline='') as csvfile:
            header_add=False
            writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        
    data.clear()
        
t1 = threading.Thread(name = "potentiometer", target=pot)
t1.setDaemon(True)
t2 = threading.Thread(name = "ultra", target=sonic)
t2.setDaemon(True)
t3=threading.Thread(name="buzz",target=buzzers)
t3.setDaemon(True)
t1.start()
t2.start()
t3.start()
try:

    while True:
        # Wait before repeating loop
        try:
            time.sleep(40)
        except KeyboardInterrupt:
            break #keypress ocurred
        if mode=="ORD" or mode=="RDM":
            makeCSV()
        
    stop_run=True

    if mode=="ORD" or mode=="RDM":
        makeCSV()
        
        print("stopped recording...",filename)
    
    spi.close()
    buzzer.ChangeDutyCycle(0)
    p1.stop()
    p2.stop()
    p3.stop()
    light.stop()
    buzzer.stop()
    gpio.remove_event_detect(SW)
    #time.sleep(3)
    gpio.cleanup()
except KeyboardInterrupt:
    #reminder that I did email you about the keyboard interrupts for ctrl-a and ctrl-x not workingand we concluded it may be due to the pi not catching the interrupts.
    stop_run==True

    if mode=="ORD" or mode=="RDM":
        makeCSV()
        
        print("stopped recording...",filename)
    buzzer.ChangeDutyCycle(0)
    p1.stop()
    p2.stop()
    p3.stop()
    light.stop()
    buzzer.stop()
    gpio.remove_event_detect(SW)
    #time.sleep(3) #give time for everything to stop
    
    spi.close()
    gpio.cleanup()


