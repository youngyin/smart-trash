# 1. Waste saturation monitoring
Whenever the trash can is closed, an ultrasonic sensor is used to transmit the distance to the bottom of the trash to the database.

### Device
Ultrasonic sensor HC-SR04, RPi3 model B

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

# 2. Connecting to a database
Since this project is simple and uses only a small amount of data, it is structured to read and write data using Google Sheets as a database.

In order to use Google Sheets, some preparation is required.
1. Apply for Google Sheets API in Google Developer Console
2. Create a service account
3. Create a security key and save it in the source file
4. Connect to Google Drive and create a blank spreadsheet
5. Sharing spreadsheets with your service accounts
6. Edit Google Sheet URL and tab name in updatedb appropriately

# 3. Automatic opening and closing of the trash can
When a user approaches the trash can, it is recognized using an ultrasonic sensor. Then use a servo motor to open the lid of the trash can.

### Device
Ultrasonic sensor HC-SR04, Servo motor SG90, RPi3 model B

### Circuit connection
| Raspberry Pi | Ultrasonic sensor |
|:--------:|:--------:|
| 3.3V | VCC |
| GPIO27 | TRIG |
| GPIO17 | ECHO |
| ground | GND |

# 4. DEMO
<iframe width="640" height="360" src="https://www.youtube.com/watch?v=w_6GqLav7gM&feature=youtu.be" frameborder="0" gesture="media" allowfullscreen=""></iframe>

# 5. references
https://developers.google.com/sheets/?hl=ko
https://support.google.com/datastudio/answer/6283323?hl=ko
https://developers.google.com/sheets/api/quickstart/python
http://hleecaster.com/python-google-drive-spreadsheet-api/
https://m.blog.naver.com/roboholic84/220319850312
https://raspberry-pi.kr/%EC%84%9C%EB%B3%B4-%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC-%ED%8C%8C%EC%9D%B4/
