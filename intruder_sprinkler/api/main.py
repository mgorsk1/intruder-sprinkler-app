import time

from fastapi import FastAPI

from intruder_sprinkler import config
from intruder_sprinkler.devices.sprinkler import SprinklerManager

app = FastAPI()
sprinkler = SprinklerManager(config.valve.gpio)
led = SprinklerManager(config.led.gpio)

devices = [sprinkler, led]


@app.on_event('startup')
async def startup_event():
    for _ in range(3):
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)


@app.post('/on')
async def on():
    for d in devices:
        d.on()


@app.post('/off')
async def off():
    for d in devices:
        d.off()


@app.get('/status')
async def status():
    return sprinkler.status()
