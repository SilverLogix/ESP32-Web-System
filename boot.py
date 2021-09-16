import micropython
import machine
from machine import Pin

# noinspection PyArgumentList
machine.freq(240000000)
micropython.alloc_emergency_exception_buf(100)

print(str('Booting...'))
btn = Pin(35, Pin.IN)  # Gpio 35 as button

