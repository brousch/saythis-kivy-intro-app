# Find some kind of TTS functionality and assign it to ttsSpeak
# On OSX, we look for:
#     say: A TTS program included with OSX
#          http://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man1/say.1.html
#     espeak: A free TTS program for Linux, Windows and OSX
#             http://espeak.sourceforge.net/
# On Linux, we look for:
#     espeak: A free TTS program for Linux, Windows and OSX
#             http://espeak.sourceforge.net/
#     flite, A free TTS program for Linux
#            http://www.speech.cs.cmu.edu/flite/
# On Windows, we look for:
#     espeak: A free TTS program for Linux, Windows and OSX
#             http://espeak.sourceforge.net/
# On Android we use the TTS feature included with Android.
# If no TTS is found, we use notts, which just echoes the message to the console


import subprocess
from kivy.utils import platform
from components import whereis_exe

platform = platform()

def ttsSpeak_android(message):
    from jnius import autoclass
    Locale = autoclass('java.util.Locale')
    PythonActivity = autoclass('org.renpy.android.PythonActivity')
    TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
    tts = TextToSpeech(PythonActivity.mActivity, None)
    tts.setLanguage(Locale.US)
    tts.speak(message, TextToSpeech.QUEUE_FLUSH, None)

def ttsSpeak_espeak(message):
    ''' Speaks the message using espeak '''
    subprocess.call(["espeak", message])


def ttsSpeak_flite(message):
    ''' Speaks the message using flite '''
    subprocess.call(["flite", "-t", message, "play"])
    

def ttsSpeak_notts(message):
    ''' Echoes the message to the console '''
    print 'FakeTTS: %s' % message


def ttsSpeak_osx(message):
    ''' Speaks the message using built-in OSX TTS '''
    subprocess.call(["say", message])


# Default to notts
ttsSpeak = ttsSpeak_notts

# Platform-specific searches
if platform == "android":
    ttsSpeak = ttsSpeak_android
    
if platform == "macosx":
    if whereis_exe('say'):
        ttsSpeak = ttsSpeak_osx
    elif whereis_exe('espeak'):
        ttsSpeak = ttsSpeak_espeak
    
elif platform == "linux":
    if whereis_exe('espeak'):
        ttsSpeak = ttsSpeak_espeak
    elif whereis_exe('flite'):
        ttsSpeak = ttsSpeak_flite
        
elif platform == "win":
    if whereis_exe('espeak'):
        tssSpeak = ttsSpeak_espeak
        