# JetsonTest_Run
For testing all the Jetson Nano and learn the core operation for beginner

## Todo :
1. Blink/Control 4 LEDs
2. Control LED over Network (Flask - Python)

> Onces the LED Control is done then using Arduino control Hand and Body:
```
00000 - None
00001 - Left Close the rist
00010 - Left Open the rist
00011 - Left Point with index finger
00100 - Left Thums Up
00101 - Left Say Hi/Bye
00110 - Move eye left
00111 - Move eye Right
01000 - Move eye Up
01001 - Move eye Down
01010 - Right Close the rist
01011 - Right Open the rist
01100 - Right Point with index finger
01101 - Right Thums Up
01110 - Right Say Hi/Bye
```

## References 
1. https://automaticaddison.com/how-to-blink-an-led-using-nvidia-jetson-nano/


## Arduino and Jetson Nano Communication 
1 Arduino will be connected to Jetson By UART PINs and 4 More Digital Pins For Select which arduino to send data 
See this Flow Chart

![V1.0.1 Flow Chart Image]()
