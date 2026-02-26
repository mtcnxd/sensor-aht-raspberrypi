 import Client

ADAFRUIT_IO_USERNAME = 'your_username'
ADAFRUIT_IO_KEY = 'aio_with_random_string' # Your secret AIO key

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Send data to a feed named 'key_of_feed'
aio.send('key_of_feed', data_to_send)
