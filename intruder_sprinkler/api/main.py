import time

from fastapi import FastAPI

from intruder_sprinkler import config
from intruder_sprinkler.devices.sprinkler import SprinklerManager

app = FastAPI()
device = SprinklerManager(config.valve.gpio)


@app.on_event('startup')
async def startup_event():
    for _ in range(3):
        device.on()
        time.sleep(1)
        device.off()
        time.sleep(1)


@app.post('/on')
async def on():
    return device.on()


@app.post('/off')
async def off():
    return device.off()


@app.get('/status')
async def status():
    return device.status()
