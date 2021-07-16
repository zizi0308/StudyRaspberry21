import Adafruit_DHT as dht
import time

sensor = dht.DHT11
pin = 17

try:
    while True:
        (h, t) = dht.read_retry(sensor, pin)
        if h != None and t != None:
            print('Temp = {0}C / Humidity = {1}%'.format(t, h))
        else:
            print('Sensing Error')

        time.sleep(1)
except Exception as e:
    print('Error occured : {0}'.format(e))

finally:
    print('End of Program')