from setuptools import setup

APP = ['main.py']
DATA_FILES = ['sounds', 'sounds/red.wav', 'sounds/green.wav', 'sounds/yellow.wav', 'sounds/blue.wav']
OPTIONS = {
    'iconfile':'images/SimonIcon.icns',
    'argv_emulation': True,
    'packages': ['certifi'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)