import enum
import numpy as np
from numpy import arange
from math import sin
from math import pi


class SignalState(enum.Enum):
    HARMONIC = 0
    DIGITAL = 1

# constants
AMPLITUDE = 5
STEP = 0.001
PHASE = 0
MAX_TIME = 1
TIME_OF_SIGNAL = arange(start=0, stop=MAX_TIME, step=STEP)

def sum_for_digital(t, c_f):
    s = 0
    for i in arange(start=1, stop=1000, step=1):
        s += sin(c_f * t * (2 * i - 1)) / (2 * i - 1)
    if s <= 0:
        return 0
    return s

class Signal(object):
    def __init__(self, frequency: float, signal_type: SignalState):
        self.frequency = frequency
        self.signal_type = signal_type

    def create_arr_of_point_for_signal(self):
        cycle_frequency = 2 * pi * self.frequency
        points = [[],[]]
        if self.signal_type == SignalState.HARMONIC:
            for t in TIME_OF_SIGNAL:
                points[0].append(t)
                points[1].append(AMPLITUDE * sin(cycle_frequency * t + PHASE))
        else:
            for t in TIME_OF_SIGNAL:
                points[0].append(t)
                points[1].append(AMPLITUDE * 4 / pi * sum_for_digital(t, cycle_frequency))
        return points

    def create_arr_of_point_for_spectrum(self):
        cycle_frequency = 2 * pi * self.frequency
        points = [[],[]]
        signal_res = []

        if self.signal_type == SignalState.HARMONIC:
            for t in TIME_OF_SIGNAL:
                signal_res.append(AMPLITUDE * sin(cycle_frequency * t + PHASE))

            points[1].append(np.abs(np.fft.fft(signal_res)))
            points[0].append(np.fft.fftfreq(len(signal_res), d=STEP))
        else:
            for t in TIME_OF_SIGNAL:
                signal_res.append(AMPLITUDE * 4 / pi * sum_for_digital(t, cycle_frequency))

            points[1].append(np.abs(np.fft.fft(signal_res)))
            points[0].append(np.fft.fftfreq(len(signal_res), d=STEP))

        return points