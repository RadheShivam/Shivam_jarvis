import os
import eel

from engine.features import playAssistantSound

from engine.command import takecommand, speak


eel.init("www")
playAssistantSound()


os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)
