import re


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



