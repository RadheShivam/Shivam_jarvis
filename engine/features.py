from email.utils import quote
import os
import sqlite3
import struct
import subprocess
import time
import webbrowser
import re


from playsound import playsound
import eel
import pvporcupine
import pyaudio
import pyautogui
import pywhatkit as kit
from engine.command import speak
from engine.config import ASSISTANT_NAME


from engine.helper import extract_yt_term, remove_words
from hugchat import hugchat

# ✅ Connect to database (USE REAL PATH)
conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()


# ✅ Play assistant start sound
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound1.mp3"
    playsound(music_dir)


# ✅ Open application or website
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query = query.lower().strip()

    if query == "":
        speak("Nothing to open")
        return

    try:
        # 🔹 Check system apps
        cursor.execute("SELECT path FROM sys_command WHERE name = ?", (query,))
        result = cursor.fetchone()

        if result:
            speak("Opening " + query)
            os.startfile(result[0])
            return

        # 🔹 Check websites
        cursor.execute("SELECT url FROM web_command WHERE name = ?", (query,))
        result = cursor.fetchone()

        if result:
            speak("Opening " + query)
            webbrowser.open(result[0])
            return

        # 🔹 Try directly opening
        speak("Opening " + query)
        os.system("start " + query)

    except Exception as e:
        print(e)
        speak("Something went wrong")


# ✅ Play YouTube song
def playYoutube(query):
    search_term = extract_yt_term(query)

    if search_term:
        speak("Playing " + search_term + " on YouTube")
        kit.playonyt(search_term)
    else:
        speak("I could not understand what to play")


def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    try:

        # pre trained keyword
        porcupine = pvporcupine.create(keyword=["jarvis", "alexa"])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length,
        )

        # loop for streaming
        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)

            # processing keyword comes from mic
            keyword_index = porcupine.process(keyword)

            # checking first keyword detected for not

            if keyword_index >= 0:
                print("Hotword Detection")

                import pyautogui as autogui

                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")

    except Exception:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

# ✅ Find contact number


def findContact(query):


    # ASSISTANT_NAME = "Jarvis"  # Define the assistant's name
    words_to_remove = [
        ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 
        'call', 'send', 'message', 'whatsapp', 'video'
    ]
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ?  OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith("+91"):
            mobile_number_str = "+91" + mobile_number_str
        return mobile_number_str, query
    except Exception:
        speak(
            'not exist in contacts'
        )
        return 0, 0


def whatsApp(mobile_no, message, flag, name):

    if flag == 'message':
        target_tab = 12
        jarvis_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7
        message = ''
        jarvis_message = "calling to "+name
    
    else:
        target_tab = 6
        message = ''
        jarvis_message = "starting video call with "+name

    # Encode the message for url
    encoded_message = quote(message)

    # Construct  the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Execute the command to open WhatsApp
    

    # Open whatsapp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)

    pyautogui.hotkey('ctrl', 'f')
    
    target_tab = 1  # Define target_tab with an appropriate value
    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter') 
    speak(jarvis_message)



# Chat bot
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path=r"engine\\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    print(response)
    speak(response)
    return response


# android automation

def makeCall(name, mobile_No):
    mobileNo = mobile_No.replace(" ", "")
    speak("Calling "+name)
    command = (
        f'adb shell am start -a android.intent.action.DIAL '
        f'-d tel:{mobileNo}'
    )
    os.system(command)



def sendMessage(message, mobileNo, name):

    from engine.helper import (
        replace_spaces_with_percent_s,
        goback,
        keyEvent,
        tapEvent,
        adbInput,
    )
    message = replace_spaces_with_percent_s(message)
    mobileNo = replace_spaces_with_percent_s(mobileNo)
    speak("sending message")
    goback(4)
    time.sleep(1)
    keyEvent(3)  # home key

    # Open sms app
    tapEvent(280, 2254)  # coordinates of sms app

    # start chat
    tapEvent(940, 2196)  # coordinates of start chat button

    # search mobile no
    adbInput(mobileNo)

    # tap on name
    tapEvent(312, 541)  # coordinates of name

    # tap on input
    tapEvent(241, 1292)  # coordinates of input box

    # message
    adbInput(message)

    # send
    tapEvents(970, 1292)  # coordinates of send button

    speak("message sent successfully to "+name)



