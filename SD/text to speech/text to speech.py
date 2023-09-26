from gtts import gTTS
import os
import pyttsx3

# Text you want to convert to speech
text_to_convert = "Hello, Welcome."

# Initialize the gTTS object
tts = gTTS(text=text_to_convert, lang='en')  # 'en' stands for English

# Save the converted audio to a file (you can change the file format if needed, e.g., 'output.mp3')
output_file = "output.mp3"
tts.save(output_file)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# Convert and play the text as speech using pyttsx3
engine.say(text_to_convert)
engine.runAndWait()