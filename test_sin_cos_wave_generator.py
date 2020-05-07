"""This test is to check the sin wave form and cos wave form behavior"""

from sin_cos_wave_generator import wave_gen


class test_wave_gen(wave_gen):
    """This is for testing the source code"""

    wave_object = wave_gen(0, 100)
    wave_object.xaxis_generator()
    wave_object.sine_plot_generator()
    wave_object.cosine_plot_generator()