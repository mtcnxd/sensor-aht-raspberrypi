import config
from Adafruit_IO import Client
import adafruit_ahtx0
import time
import random
import board

ADAFRUIT_IO_USERNAME = config.ADAFRUIT_AIO_USERNAME
ADAFRUIT_IO_KEY = config.ADAFRUIT_AIO_KEY

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

def round(value):
    input = float(value)
    return '{:.2f}'.format(input)

sensor = adafruit_ahtx0.AHTx0(board.I2C())

time.sleep(2)

# sensor_value = random.randint(0,255)
sensor_value = sensor.temperature

if sensor_value is not None:
    sensor_value = round(sensor_value)
    print(f"The current sensor value is: {sensor_value}")
    aio.send('temperature', sensor_value)
