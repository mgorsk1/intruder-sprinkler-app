import time

from fastapi import FastAPI
from pydantic import BaseModel

from intruder_sprinkler import config
from intruder_sprinkler.devices.sprinkler import SprinklerManager

app = FastAPI()
sprinkler = SprinklerManager(config.valve.gpio)
led = SprinklerManager(config.led.gpio)

devices = [sprinkler, led]


class SwitchModel(BaseModel):
    active: bool


class StateModel(BaseModel):
    is_active: bool


@app.on_event('startup')
async def startup_event():
    for _ in range(3):
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)


@app.post('/valve')
async def on(switch: SwitchModel):
    if switch.active:
        for d in devices:
            d.on()
    else:
        for d in devices:
            d.off()


@app.get('/valve')
async def status():
    return StateModel(is_active=sprinkler.status())
