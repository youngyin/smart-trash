# 1. 모니터링

### Device
Ultrasonic sensor HC-SR04, RPi3 model B

### Circuit connection
| Raspberry Pi | Ultrasonic sensor |
|:--------:|:--------:|
| 3.3V | VCC |
| GPIO27 | TRIG |
| GPIO17 | ECHO |
| ground | GND |

# 2. google sheets api
https://developers.google.com/sheets/api

# 3. 자동 개폐

### Device
Ultrasonic sensor HC-SR04, Servo motor SG90, RPi3 model B

### Circuit connection
| Raspberry Pi | Servo motor | Ultrasonic sensor |
|:--------:|:--------:|:--------:|
| 5V | VCC |  |
| GPIO02 | sensor |  |
| ground | GND |  |
| 3.3V |  | VCC |
| GPIO20 |  | TRIG |
| GPIO26 |  | ECHO |
| ground |  | GND |
