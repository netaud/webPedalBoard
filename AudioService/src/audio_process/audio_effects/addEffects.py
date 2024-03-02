from pedalboard import Pedalboard, Chorus, Distortion, Reverb, Delay, HighpassFilter, LowpassFilter
from pedalboard import load_plugin


def addReverb(_roomSize, _damping, _wetLevel, _dryLevel, _width, _freezeMode):
    reverb = Reverb(
    room_size = _roomSize,
    damping = _damping,
    wet_level = _wetLevel,
    dry_level = _dryLevel, 
    width = _width,
    freeze_mode = _freezeMode)

    return reverb

def addDelay(_delaySeconds, _feedback, _mix):
    delay = Delay(
    delay_seconds = _delaySeconds,
    feedback = _feedback,
    mix = _mix)

    return delay

def addChorus(_rateHz, _depth, _centreDelayMs):
    chorus = Chorus(
    rate_hz = _rateHz, 
    depth = _depth, 
    centre_delay_ms =_centreDelayMs)
    
    return chorus

def addDistortion(_driveDb):

    distortion = Distortion(
    drive_db = _driveDb)

    return distortion


def addHighPass(_cutOffFrequency):
    highPasss = HighpassFilter(
    cutoff_frequency_hz = _cutOffFrequency)

    return highPasss


def addLowPass(_cutOffFrequency):
    lowPass = LowpassFilter(
    cutoff_frequency_hz = _cutOffFrequency)

    return lowPass




board = Pedalboard([
    addReverb(0,0,0,0,0,0),
    addDelay(0,0,0),
    addChorus(0,0,0),
    addDistortion(0),
    addHighPass(0),
    addLowPass(0)
    ])