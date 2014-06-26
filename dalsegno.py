import pyaudio
import scipy
import numpy

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
WAVE = 440.0
nsec = 10

#Generates a 1 second long sound wave
outdata = ''.join([chr(int(numpy.sin(x/((RATE/WAVE)/numpy.pi))*127+128)) for x in xrange(RATE)])


