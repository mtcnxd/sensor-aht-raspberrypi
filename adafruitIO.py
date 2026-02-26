import config
from Adafruit_IO import Client
import time
import random

ADAFRUIT_IO_USERNAME = config.ADAFRUIT_AIO_USERNAME
ADAFRUIT_IO_KEY = config.ADAFRUIT_AIO_KEY

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

for range_value in range(10):
    sensor_value = random.randint(0,255)
    print(f"The current sensor value is: {sensor_value} and range value: {range_value}")
    aio.send('temperature', sensor_value)
    time.sleep(1)
