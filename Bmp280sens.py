import bme280
import schedule
import time
import datetime
 
(chip_id, chip_version) = bme280.readBME280ID(0x76)
#print "Chip ID :", chip_id
#print "Version :", chip_version
 
def altitude(pressure,temperature):
    p0=1013.25
    num=((p0/pressure)**(1/5.257)-1)*(temperature+273.15)
    den=.0065
    return (num/den)

def getTimestamp():
    now=datetime.datetime.now()
    print(now)
    

def stats():
    print "temperature : ", temperature,"C"
    print "pressure : %.3f" % pressure + " hPa"
    print "altitude : %.3f" % altitude(pressure,temperature) + " m"
    print "timestamp : ", getTimestamp()


while True:
    temperature,pressure,humidity = bme280.readBME280All()
    stats()
    time.sleep(10)


    
