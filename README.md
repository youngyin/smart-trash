# 1. IoT sensor based development of smart-trash-box


# 2. Waste saturation monitoring
초음파 센서를 이용하여 쓰레기통 바닥까지의 거리 값을 데이터베이스로 전송한다. 사용자는 웹서비스를 통해 쓰레기통의 사용 가능 여부를 모니터링한다.

### Device
Ultrasonic sensor HC-SR04, RPi3 model B<br>
<img src="https://user-images.githubusercontent.com/57608725/102043378-8e72f300-3e17-11eb-80d9-daac20e8ecfb.jpg" width="60%"></img>

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

### DEMO

# 3. Automatic opening and closing of the trash can
사용자가 쓰레기통 근처에 다가가면 초음파 센서를 이용하여 이를 인지하고 서보모터를 활용하여 쓰레기통의 뚜껑을 연다.

### Device
Ultrasonic sensor HC-SR04, Servo motor SG90, RPi3 model B<br>
<img src="https://user-images.githubusercontent.com/57608725/102043379-8fa42000-3e17-11eb-9020-9e99ef0c0805.jpg" width="90%"></img>

### Circuit connection
| Raspberry Pi | Ultrasonic sensor |
|:--------:|:--------:|
| 3.3V | VCC |
| GPIO20 | TRIG |
| GPIO26 | ECHO |
| ground | GND |

### DEMO

# 4. Project expected effect
도시 및 환경관리자로 하여금 쾌적한 환경계획을 위하여 효율적인 쓰레기 수거계획 및 쓰레기통 배치 계획의 인사이트를 제공하고자 한다. 
사용자로 하여금 쓰레기통이 넘치는 것을 방지하고 직접 쓰레기통에 손을 대지 않아도 사용이 가능하도록 하여 청결하고 안전한 도시에 기여하고자 한다.

# 5. references
