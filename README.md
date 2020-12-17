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

# 5. DEMO

# 4. references
Various internet resources were referenced to control the devices used in the project, and links to the site were included in the code.
