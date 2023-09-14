import enum
from numpy import arange
from math import cos, sin
from math import pi
from numpy import sign


class SignalState(enum.Enum):
    HARMONIC = 0
    DIGITAL = 1


# constants
AMPLITUDE = 5
STEP = 0.001
PHASE = 0
MAX_TIME = 10


class Signal(object):
    def __init__(self, frequency: float, signal_type: SignalState):
        self.frequency = frequency
        self.signal_type = signal_type

    def create_arr_of_point_for_signal(self):
        cycle_frequency = 2 * pi * self.frequency
        points = [[],[]]
        if self.signal_type == SignalState.HARMONIC:
            for t in arange(start=0, stop=MAX_TIME, step=STEP):
                points[0].append(t)
                points[1].append(AMPLITUDE * cos(cycle_frequency * t + PHASE))
        else:
            for t in arange(start=0, stop=MAX_TIME, step=STEP):
                points[0].append(t)
                points[1].append(AMPLITUDE * 4 / pi * self.sum_for_digital(t, cycle_frequency))
        return points

    def sum_for_digital(self, t, c_f):
        s = 0
        for i in arange(start=1, stop=1000, step=1):
            s += sin(c_f*t*(2*i-1))/(2*i-1)
        return s

