import logging

from gpiozero import DigitalOutputDevice


class BaseOutputDeviceManager:
    def __init__(self, gpio: int):
        self.device = DigitalOutputDevice(gpio)

    def on(self):
        if not self.status():
            self.device.on()
        else:
            logging.warning('device was already on.')

    def off(self):
        if self.status():
            self.device.off()
        else:
            logging.warning('device was already off.')

    def status(self):
        # true > active, false > inactive
        return self.device.is_active
