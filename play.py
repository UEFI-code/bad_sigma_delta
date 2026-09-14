import serial
import threading
import numpy as np
import demo2
import time

#ser = serial.Serial('/dev/ttyUSB0', 115200)
target_value = 0

def worker():
    global target_value
    while True:
        demo2.sigma_delta_step(target_value)
        value = demo2.get_byte_value()
        print(f"Byte value: {value:08b}")
        #ser.write(bytes([value]))
        #time.sleep(1)  # Adjust the sleep time as needed

thread = threading.Thread(target=worker)
thread.start()

# generate a 440Hz sine wave for 1 second
fs = 44100  # sample rate
f = 440.0  # frequency
samples = (np.sin(2 * np.pi * np.arange(fs) * f / fs)).astype(np.float32)

while True:
    for sample in samples:
        target_value = sample * 0.5 + 0.5  # scale to [0, 1]
        time.sleep(1/fs)  # wait for the next sample