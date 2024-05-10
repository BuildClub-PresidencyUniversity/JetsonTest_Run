import time
import Jetson.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)


GPIO.setup(7, GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

try:
    while True:
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(11, GPIO.HIGH)
  
        time.sleep(1)
     
        GPIO.output(7, GPIO.LOW)
        GPIO.output(11,GPIO.LOW)

  
        time.sleep(1)

except KeyboardInterrupt:
 
    GPIO.cleanup()

