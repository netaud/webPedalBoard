import soundfile as sf
from audioEffects.addEffects import *

samples, sampleRate = sf.read("PATH")

if (len(samples.shape) == 2):

    leftChannel = samples[:, 0]
    rightChannel = samples[:, 1]
    mono = leftChannel + rightChannel

    wet = board(mono, sampleRate, buffer_size=len(mono))
else:

    wet = board(samples, sampleRate, buffer_size=len(samples))

sf.write('NEW.wav', wet, sampleRate)