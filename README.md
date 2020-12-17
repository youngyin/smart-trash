# 1. Waste monitoring

### Device
Ultrasonic sensor HC-SR04, RPi3 model B

### Circuit connection
| Raspberry Pi | Ultrasonic sensor |
|:--------:|:--------:|
| 3.3V | VCC |
| GPIO27 | TRIG |
| GPIO17 | ECHO |

# 2. Connecting to a database
google sheets api: https://developers.google.com/sheets/api

# 3. Automatic opening and closing of the trash can

### Device
Ultrasonic sensor HC-SR04, Servo motor SG90, RPi3 model B

### Circuit connection
| ground | GND |
| Raspberry Pi | Servo motor | Ultrasonic sensor |
|:--------:|:--------:|:--------:|
| 5V | VCC |  |
| GPIO02 | sensor |  |
| ground | GND |  |
| 3.3V |  | VCC |
| GPIO20 |  | TRIG |
| GPIO26 |  | ECHO |
| ground |  | GND |

# 4. DEMO
[![Video Label](https://i9.ytimg.com/vi/w_6GqLav7gM/mq1.jpg?sqp=CLyf7v4F&rs=AOn4CLBvJ1WaO5Fv0ooPz2ORO2hc042E9g)](https://www.youtube.com/watch?v=w_6GqLav7gM&feature=youtu.be)
