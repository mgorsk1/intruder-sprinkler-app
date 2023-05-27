from fastapi import FastAPI

from intruder_sprinkler import config
from intruder_sprinkler.devices.sprinkler import SprinklerManager

app = FastAPI()
device = SprinklerManager(config.valve.gpio)


@app.post('/on')
async def on():
    return device.on()


@app.post('/off')
async def off():
    return device.off()


@app.get('/status')
async def status():
    return device.status()
