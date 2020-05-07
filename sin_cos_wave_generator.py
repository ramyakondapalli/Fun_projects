""" This module generates sin and cos wave for generated numbers
 This module also uses numpy and matplotlib libraries"""

import numpy as np
import matplotlib.pyplot as mp


class wave_gen(object):
    """ This class has functions to plot sine wave and cos wave """

    def __init__(self, low_limit, up_limit):
        self.low_limit = low_limit
        self.up_limit = up_limit
        self.step_size = 0.5

    def xaxis_generator(self):
        """ This function generates floating point numbers between low_limit and up_limit at step of 0.25"""
        X = np.arange(self.low_limit, self.up_limit, self.step_size)
        return X

    def sine_plot_generator(self):
        """ This function generates requested wave form for the x - axis generated in the previous function"""
        Y = np.sin(self.xaxis_generator())
        return mp.plot(self.xaxis_generator(), Y)

    def cosine_plot_generator(self):
        """ This function generates requested wave form for the x - axis generated in the previous function"""
        Y = np.cos(self.xaxis_generator())
        return mp.plot(self.xaxis_generator(), Y)

