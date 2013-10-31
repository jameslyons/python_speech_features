.. python_speech_features documentation master file, created by
   sphinx-quickstart on Thu Oct 31 16:49:58 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to python_speech_features's documentation!
==================================================

This library provides common speech features for ASR including MFCCs and filterbank energies.
If you are not sure what MFCCs are, and would like to know more have a look at this [MFCC tutorial](http://www.practicalcryptography.com/miscellaneous/machine-learning/guide-mel-frequency-cepstral-coefficients-mfccs/).


You will need numpy and scipy to run these files.

To use MFCC features,

```python
from mfcc import mfcc
from mfcc import fbank
import scipy.io.wavfile as wav

(rate,sig) = wav.read("/file.wav")
mfcc_feat = mfcc(sig,rate)
fbank_feat = fbank(sig,rate)
```

From here you can write the features to a file etc.

Functions provided in mfcc module
---------------------------------
   
.. automodule:: mfcc
    :members:
    

Functions provided in sigproc module
------------------------------------
.. automodule:: sigproc
    :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`

