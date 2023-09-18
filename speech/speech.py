import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Please speak something...")
    audio = recognizer.listen(source)

try:
    # Recognize the speech using Google Web Speech API
    text = recognizer.recognize_google(audio)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand your audio.")
except sr.RequestError as e:
    print(f"Sorry, there was an error connecting to the Google API: {e}")


# Define a dictionary of common text abbreviations and their expansions
abbreviations = {
    "r": "are",
    "u": "you",
}

# Function to replace abbreviations with their expansions
def replace_abbreviations(text, abbreviation_dict):
    words = text.split()
    expanded_words = [abbreviation_dict.get(word, word) for word in words]
    expanded_text = " ".join(expanded_words)
    return expanded_text

# Convert the input text
output_text = replace_abbreviations(text, abbreviations)

# Print the result

print("You Said: ")

for txt in output_text:

    print(txt,'\n')
