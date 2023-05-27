from fastapi import FastAPI

from intruder_sprinkler import config
from intruder_sprinkler.devices.sprinkler import SprinklerManager

app = FastAPI()
sprinkler = SprinklerManager(config.valve.gpio)
led = SprinklerManager(config.led.gpio)

devices = [sprinkler, led]


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
