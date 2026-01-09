import os
import re
import time


def extract_yt_term(command):
    # Define a regular expression patter to capture the sonr name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # Use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    # If a match is found, return the extracted song name; otherwise, return None
    return match.group(1) if match else None


def remove_words(input_string, words_to_remove):
    #Slpit the input string into words
    words = input_string.split()

    #remove unwanted words
    filtered_words = [
        word for word in words if word.lower() not in words_to_remove
    ]

    # Join the remaininwords back into a string
    result_string = ' '.join(filtered_words)

    return result_string


# # Example usage
# input_string = "make a phone call to papa"
# words_to_remove = ["make", "a", "phone", "call", "to",'send','message','email','mail']

# result = remove_words(input_string, words_to_remove)
# print(result)


# find contacts

# key events like receive call, stop call, go back
def keyEvent(key_code):
    command = f'adb shell input keyevent {key_code}'
    os.syastem(command)
    time.sleep(1)

# Tap event used to tap anywhere
def tapEvent(x, y):
    command = f'adb shell input tap {x} {y}'
    os.system(command)
    time.sleep(1)

# Input Event is used to insert text in mobile
def adbInput(message):
    command = f'adb shell input text "{message}"'
    os.system(command)
    time.sleep(1)


# to go complete back
def goback(key_code):
    for i in range(6):
        keyEvent(key_code)   # type: ignore


# to replace space in string with %s for complete message send

def replace_spaces_with_percent_s(input_string):
    return input_string.replace(' ', '%s')



