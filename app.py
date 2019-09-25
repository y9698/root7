from flask import Flask, render_template, request
#from flask import requests
#from tensorflow.keras.datasets import mnist
import requests
#import request
import json
import jsonify
import numpy as np
#import matplotlib.pyplot as plt
import io 
import urllib.request
from PIL import Image


#import io 
#import urllib.request
#from PIL import Image

# 画像のURL 今回はPythonのロゴを使用
#url = "https://www.python.org/static/img/python-logo@2x.png"
# 画像データを取得する
#img_in = urllib.request.urlopen(url).read()
#img_bin = io.BytesIO(img_in)
# Pillowで開き、画像を保存する
#img = Image.open(img_bin)
#img.save("logo.png","PNG")
# 以下のコメントを外すとバイナリデータそのものを確認できる
# print(img_bin.getvalue())


app = Flask(__name__)

@app.route('/')
def sample():
    name = 'heroku upload test'
    return render_template('index.html', name=name)

@app.route('/index2', methods=["POST"])
def index2():
    x_test = request.form['img_file']

    x_test = io.BytesIO(x_test)
    # Pillowで開き、画像を保存する
    x_test = Image.open(x_test)


    img_rows, img_cols = 28, 28

    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    x_test = x_test.astype('float32')
    x_test /= 255

    test = x_test
    test = (np.epand_dims(test,0))

    data = {
        'images': test.tolist()
    }


    API_URL = 'https://root67.herokuapp.com/'
    res = requests.post(API_URL, json=data)

    result = []
    for v in res :
        try:
            js = json.loads(v)
            result.append( js['data'] )
        except Exception:
            pass

    result = int(result[0]['prediction'][0])
    #print("もしかしたら：",result,"？かも")

    return render_template("index2.html", result = result)




if __name__ == '__main__':
    app.run(debug=True)