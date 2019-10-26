# from base64 import decodebytes
# from PIL import Image
import base64
from flask import Flask, flash, render_template, redirect, request, url_for,jsonify
from PIL import Image
from io import BytesIO

app = Flask(__name__)
app.secret_key = "b1234567"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/saveImage', methods=['GET','POST'])
def saveImage():
    if request.method == 'POST':
        image = request.get_json()
        imagestr = image['text']
        print(imagestr[22:])
        imagestr = imagestr[22:]
        # if len(imagestr) %4 != 0:
        #     while len(imagestr) % 4 != 0:
        #         imagestr = imagestr + "="
        # else:
        #     req_str = base64.b64decode(imagestr)
        inputIm = Image.open(BytesIO(base64.b64decode(imagestr)))
        im = Image.new("RGB", inputIm.size, "WHITE")
        im.paste(inputIm, (0, 0), inputIm)
        im.save('image.png', 'PNG')
        return jsonify(image)
    return redirect(url_for('index'))