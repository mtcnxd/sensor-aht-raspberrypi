# import adafruit_ahtx0
# import board
import time
import datetime

# sensor = adafruit_ahtx0.AHTx0(board.I2C())

def round_num(input):
   return '{:.2f}'.format(input)


# print(sensor.temperature)
# print(sensor.relative_humidity)


if __name__ == "__main__":
   time.sleep(2)

   now = datetime.datetime.now()
   print(now)