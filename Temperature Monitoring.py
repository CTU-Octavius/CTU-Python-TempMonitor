import random
import time
import logging
from datetime import datetime
 
logging.basicConfig(
    filename="temperature_log.txt",
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)
 
def generate_temperature():
    if random.random() < 0.05:
        message = "Sensor failure detected! Retrying..."
        print(message)
        logging.info(message)
        return generate_temperature()
   
    temperature = random.uniform(20, 150)
   
    if temperature < 50 or temperature > 120:
        message = f"Warning: temperature too hot or too cold temperature detected! ({temperature:.2f}°C)"
    else:
        message = f"Temperature is safe: {temperature:.2f}°C"
   
    print(message)
    logging.info(message)
   
    return temperature
 
def monitor_temperature():
    for _ in range(100):
        time.sleep(0.01)
        generate_temperature()
        continue
 
monitor_temperature()
 
 