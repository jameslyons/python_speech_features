import scipy.io.wavfile as wav

from features import mfcc
from features import logfbank


(rate, sig) = wav.read("file.wav")
mfcc_feat = mfcc(sig, rate)
fbank_feat = logfbank(sig, rate)

print fbank_feat[1:3, :]
