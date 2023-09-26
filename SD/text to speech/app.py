from flask import Flask,render_template,request
from gtts import gTTS
import os
import pyttsx3
import speech_recognition as sr
from pydub import AudioSegment


app = Flask(__name__, static_folder='static')

@app.route('/')
def index_view():
    return render_template('index.html')

imgfold = os.path.join('static', 'images') 

recognizer = sr.Recognizer()


@app.route('/getInput',methods=['GET','POST'])
def showtext():
    if request.method == 'POST':
        text_to_convert = request.form.get('text')

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

        return render_template('index.html')
    
if __name__  == '__main__':
    app.run(debug=True)