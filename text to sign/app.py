from flask import Flask,render_template,request
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index_view():
    return render_template('index.html')

imgfold = os.path.join('static', 'images') 

@app.route('/getInput',methods=['GET','POST'])
def showtext():
    if request.method == 'POST':
        text = request.form.get('text')
        text = text.lower()
        if (text=="hii" or text=="hello"):
            text = "hi"
        filename = text+".jpg"
        imgUrl = os.path.join(imgfold, filename)
        if not os.path.exists(imgUrl):
            filename = text+".png"
            imgUrl = os.path.join(imgfold, filename)

        return render_template('index.html',url=imgUrl)
    
if __name__  == '__main__':
    app.run(debug=True)