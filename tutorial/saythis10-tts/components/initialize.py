# Perform platform-specific initializations
# On Android:
#     Set up jnius
#     Set locale

from kivy.utils import platform

platform = platform()

def initialize_android():
    from jnius import autoclass
    PythonActivity = autoclass('org.renpy.android.PythonActivity')
    AudioManager = autoclass('android.media.AudioManager')
    PythonActivity.mActivity.setVolumeControlStream(AudioManager.STREAM_MUSIC)

def initialize_other():
    pass

# Default to no platform-specific initialization
initialize_platform = initialize_other

# Platform-specific searches
if platform == "android":
    initialize_platform = initialize_android
