# RPIclient

**Requirements**
---
- Python 3.8
- BME280 sensor
- Raspberry Pi 3+ (or any model that supports sensor)

**Description**
---
This application reads temperature and pressure from our sensor and calculates altitude using the hypsometric formula. The data is collected every ten seconds and posted to our 
database. 

**Quick Start**
---
Clone and pull main branch. To modify to your own project, provide your own database url in the httpclient.py as well as username and password. To run, just running the main.py 
file will allow the application to start posting.
