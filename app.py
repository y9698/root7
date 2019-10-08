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
from tensorflow.python.keras.preprocessing.image import array_to_img, img_to_array, load_img
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
def sample2():
    name2 = "here is index2"
    pic = request.form['img_file']
    test =img_to_array(load_img(pic, target_size=(28,28), color_mode = "grayscale"))
# for test in tests:
#     x.append(test)
   

#test = x.reshape(1,2352)
x=np.asarray(test)
# print("shape===", x.shape)

#x= np.squeeze(x)
#x=np.asarray(x)
x=x.astype('float32')
#x=x.reshape(2352,1)
x = 1-x/255.0
x = (np.expand_dims(x,0))
#print("x;",x)
# print('x:',x)
    # x_test = io.BytesIO(x_test)
    # # Pillowで開き、画像を保存する
    # x_test = Image.open(x_test).convert('L')


    # img_rows, img_cols = 28, 28

    # x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    # x_test = x_test.astype('float32')
    # x_test /= 255
    #x_test = 1- np.array(x_test)
    #X_test = x_test.reshape(1,784)

    # test = x_test
    # test = (np.expand_dims(test,0))

    data = {
        'images': x.tolist()
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

    return render_template("index2.html", result = result, name2=name2)




if __name__ == '__main__':
    app.run(debug=True)