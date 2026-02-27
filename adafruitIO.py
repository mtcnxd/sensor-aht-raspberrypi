from Adafruit_IO import Client
import adafruit_ahtx0
import config
import time
import board
import datetime

ADAFRUIT_IO_USERNAME = config.ADAFRUIT_AIO_USERNAME
ADAFRUIT_IO_KEY = config.ADAFRUIT_AIO_KEY

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

def round(value):
    input = float(value)
    return '{:.2f}'.format(input)

def sendDataIO(topic, value):
    try:
        aio.send(topic, value)
        print(f"Data sent to Adafruit IO: {topic} - {value}")
    except Exception as e:
        print(f"Error sending data to Adafruit IO: {e}")

sensor = adafruit_ahtx0.AHTx0(board.I2C())
time.sleep(2)

temperature = sensor.temperature
humid = sensor.relative_humidity

if temperature is not None:
    temperature = round(temperature)
    sendDataIO('temperature', temperature)

if humid is not None:
    humid = round(humid)
    sendDataIO('humidity', humid)

print(f"Finished at: {datetime.datetime.now()}")
