import time
import board
import adafruit_dht
from gpiozero import LED
from w1thermsensor import W1ThermSensor

red = LED(17)
yellow = LED(27)
green = LED(22)
dhtDevice = adafruit_dht.DHT11(board.D18)
sensor = W1ThermSensor()
volgnummer = 0

while True:
    try:
        temperature_in_celcius = sensor.get_temperature()
        temperature_c = dhtDevice.temperature

        verschil = temperature_c - temperature_in_celcius
        if verschil < 1:
            green.on()
            yellow.off()
            red.off()
            print(f"{volgnummer}: DHT11 = {temperature_c}, w1thermsensor = {temperature_in_celcius}, groene LED gaat branden")
            volgnummer += 1
        elif verschil < 5 and (verschil >= 1):
            yellow.on()
            green.off()
            red.off()
            print(f"{volgnummer}: DHT11 = {temperature_c}, w1thermsensor = {temperature_in_celcius}, gele LED gaat branden")
            volgnummer += 1
        else:
            red.on()
            yellow.off()
            green.off()
            print(f"{volgnummer}: DHT11 = {temperature_c}, w1thermsensor = {temperature_in_celcius}, rode LED gaat branden")
            volgnummer += 1
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue

    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)