from mfcc import mfcc
from mfcc import fbank
import scipy.io.wavfile as wav

(rate,sig) = wav.read("file.wav")
mfcc_feat = mfcc(sig,rate)
fbank_feat = fbank(sig,rate)

print mfcc_feat[1:3,:]
