import os
from flask import Flask, render_template, Response, make_response, request,send_file
# from camera_opencv_main import mainCamera,sideICamera,sideIICamera
from maincamera import mainCamera
from sideIcamera import sideICamera
from sideIIcamera import sideIICamera
from error_msg import ERRORMSG
import json
from flask_cors import *
app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

class ProcessExpection(Exception):
    '''
    ProcessExpection 是一个继承于 Exception 类的异常类,用于处理 各种 模块遇到的异常
    '''
    def __init__(self,error):
        self.error_msg = error
    def __str__(self):
        return ("Error occurred::{}".format(self.error_msg))

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

@app.route('/nosignal')
def send_nosignal():
    return send_file("./img/nosignal.jpg",mimetype='image/gif')

def gen(camera):
    """Video streaming generator function."""
    yield b'--frame\r\n'
    while True:
        frame = camera.get_frame()
        yield b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n--frame\r\n'


@app.route('/video_source_1')
def video_source_1():
    return Response(gen(mainCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_source_2')
def video_source_2():
    return Response(gen(sideICamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_source_3')
def video_source_3():
    return Response(gen(sideIICamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/api/setting',methods=['GET','POST'])
def returnSetting():
    jsonobj = 0
    print("Was called")
    with open("status.json","r") as f:
        jsonobj = json.load(f)
    res = make_response(jsonobj)
    res.headers['Access-Control-Allow-Origin']='*'
    return res
@app.route('/api/updatesetting',methods=['GET','POST'])
def updateSetting():
    with open("status.json","w") as f:
        to_dump = request.data.decode()
        print(to_dump)
        json.dump(to_dump,f)
    return Response(status=200)

@app.route('/api/getsrc',methods=['GET','POST'])
def returnVideosrc():
    if os.path.exists("./img/.ok"):
        videosrc={"body":[
            "http://127.0.0.1:5000/video_source_1",
            "http://127.0.0.1:5000/video_source_2",
            "http://127.0.0.1:5000/video_source_3"
        ]}
    else:
        videosrc={"body":[
            "http://127.0.0.1:5000/nosignal",
            "http://127.0.0.1:5000/nosignal",
            "http://127.0.0.1:5000/nosignal"
        ]}
    res = make_response(json.dumps(videosrc))
    res.headers['Access-Control-Allow-Origin']='*'
    return res

@app.route('/api/postcommand',methods=['GET','POST'])
def runcommand():
    j = json.loads(request.data.decode())
    res = {}
    command = j['body']
    try:
        res_code = os.system(command)
        if res_code!=0:
            raise ProcessExpection(ERRORMSG[res_code])
        res['error'] = 0
        res['errormsg'] = "OK"
    except Exception as e:
        print(e)
        res['error'] = 1
        res['errormsg'] = str(e)
    return make_response(res)
if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)