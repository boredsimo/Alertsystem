import i2c_lcd_driver
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
mylcd = i2c_lcd_driver.lcd()
Gpin=16
Rpin=18
Pin = 13
state=1
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(Gpin,GPIO.OUT)
GPIO.setup(Rpin,GPIO.OUT)
mylcd.lcd_display_string("", 1)
def alert(x):
    mylcd.lcd_display_string("Alerte au feu!!!!!", 1)
    GPIO.output(Rpin,state)
    sleep(2)
    GPIO.output(Rpin,not state)
    mylcd.lcd_display_string("Pas de feu!!!", 1)
    GPIO.output(Gpin,state)
    sleep(2)
    GPIO.output(Gpin,not state)
    
    

def loop():
    GPIO.add_event_detect(Pin,GPIO.FALLING,callback=alert)
    while True:
        pass


try:
    loop()
except KeyboardInterrupt:
    print("The end!")

