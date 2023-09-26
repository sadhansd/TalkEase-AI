from flask import Flask, render_template, request
import os
import speech_recognition as sr
import urllib.parse


app = Flask(__name__, static_folder='static')


@app.route('/')
def index_view():
    return render_template('index.html')

imgfold = os.path.join('static', 'images')
recognizer = sr.Recognizer()
note = "Please speak something..."


@app.route('/showimg', methods=['GET', 'POST'])
def showimg():
    if request.method == 'POST':

        with sr.Microphone() as source:
            print(note)
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

        if (output_text == "hi" or output_text == "hello"):
            output_text = "hi"
        output_text = urllib.parse.unquote(output_text)
        filename = output_text + ".jpg"
        imgUrl = os.path.join(imgfold, filename)
        if not os.path.exists(imgUrl):
            filename = text + ".png"
            imgUrl = os.path.join(imgfold, filename)

    return render_template('index.html', text=note, url=imgUrl)


if __name__ == '__main__':
    app.run(debug=True)




# Print the result

print("You Said: ")
print(output_text)
