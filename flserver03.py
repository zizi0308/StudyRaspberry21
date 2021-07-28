# index.html 로딩서버
from flask import Flask, render_template

# Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/')  # 접속하는 최초 url
def index():
    # 백엔드에서 만든 데이터를 프론트엔드에 전달
    return render_template('info.html', user='조희지', data={'userid' : 'zizi0308', 'gender' : 'female', 'age':26})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)