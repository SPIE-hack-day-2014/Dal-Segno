import pyaudio
import scipy
import numpy
import pyfits
import matplotlib.pyplot as pyplot


fig = pyplot.figure(0)
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
WAVE = 440.0
nsec = 10

#Generates a 1 second long sound wave
outdata = ''.join([chr(int(numpy.sin(x/((RATE/WAVE)/numpy.pi))*127+128)) for x in xrange(RATE)])

data = pyfits.getdata('')


