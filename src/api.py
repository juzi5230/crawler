# from flask import Flask

# app = Flask(__name__)

# @app.route('/hello')
# def hello():
#     return '122313231'

# print('....' + __name__)
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=6000)


from flask import Flask, jsonify, send_file

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

# ＃ 普通的文本接口
@app.route('/text')
def text ():
  return '您正在访问Python写的接口'


@app.route('/json')
def return_json():
  data = {'msg': 'this is a jsonstr'}
  return jsonify(data)

@app.route('/image')
def return_image():
  imgPath = '/Users/cheng/Downloads/edit@2x.png'
  return send_file(imgPath, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)