import adafruit_ahtx0
import board
import time
import datetime

sensor = adafruit_ahtx0.AHTx0(board.I2C())

def round_num(input):
   return '{:.2f}'.format(input)

#print('Temperature', round_num(sensor.temperature), 'C')
#print('Humidity', round_num(sensor.relative_humidity), '%')

time.sleep(2)

print(sensor.temperature)

print(sensor.relative_humidity)

now = datetime.datetime.now()

print(now)
