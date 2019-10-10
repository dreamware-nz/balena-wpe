import time
import requests
import logging

logging.info("RAL is alive")
try:
    # r = requests.get('http://uix:5000')
    r = requests.get("https://www.stuff.co.nz")
    logging.info(r.text)
except:
    pass
time.sleep(30)
