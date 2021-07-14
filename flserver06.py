# index.html 로딩서버
from flask import Flask, render_template, request

# Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/')  # 접속하는 최초 url
def index():
    # 백앤드에서 프론트앤드로 전달
    return render_template('login.html')

@app.route('/get', methods=['GET'])
def get():
    user = request.args.get('user')
    msg = "{0}".format(user)
    return msg

@app.route('/post', methods=['POST'])   # route(경로)를 받아서 처리하는 부분이 controller
def post():
        userid = request.form.get('userid')
        password = request.form.get('password')
        msg = "{0} / {1}".format(userid, password)
        friends = ['Kim', 'Jo', 'Lee']
    # 백엔드에서 만든 데이터를 프론트엔드에 전달
        return render_template('result.html', result=msg, friends=friends)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)    # debug를 위한 파라미터추가 >> debug=True