try:
    from setuptools import setup #enables develop
except ImportError:
    from distutils.core import setup

setup(name='python_speech_features',
<<<<<<< 475e99f610f38fc3dfc8361f5bc21cf8c1dfd6f3
      version='0.4',
=======
      version='0.2',
>>>>>>> changed naming for pypi release
      description='Python Speech Feature extraction',
      author='James Lyons',
      author_email='james.lyons0@gmail.com',
      license='MIT',
      url='https://github.com/jameslyons/python_speech_features',
      packages=['python_speech_features'],
    )
