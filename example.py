#!/usr/bin/env python

import librosa
from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
import scipy.io.wavfile as wav

(rate,sig) = wav.read("english.wav")
mfcc_feat = mfcc(sig,rate)
d_mfcc_feat = delta(mfcc_feat, 2)
fbank_feat = logfbank(sig,rate)

print(fbank_feat[1:3,:])


# stride = 10 ms
# sample_rate = 8K
# hop_length = stride * sample_rate 
assert librosa.samples_to_frames(1200000, hop_length=80) == 15000
assert librosa.samples_to_frames(1280000, hop_length=80) == 16000
assert librosa.frames_to_samples(16000, hop_length=80) == 1280000

assert librosa.time_to_frames(10, sr=8000, hop_length=80) == 1000
assert librosa.time_to_frames(300.29, sr=8000, hop_length=80) == 30029
assert librosa.frames_to_time(30029, hop_length=80, sr=8000) ==300.29 

assert librosa.samples_to_times(80000, sr=8000) == 10.0
assert librosa.time_to_samples(10.0, sr=8000) == 80000 
