import os
import subprocess
import eel

from engine.features import playAssistantSound
from engine.command import takecommand, speak

from engine.auth import recoganize


def start():

    eel.init("www")
    
    playAssistantSound()
    @eel.expose
    def init():
        subprocess.call(r'device.bat')
        eel.hideLoader()
        speak('Ready for face Authentication')

        flag = recoganize.AuthenticateFace()
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful.")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome sir.")
            eel.hideStart()
        else:
            speak("Face Authentication Failed.")

    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)