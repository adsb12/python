from flask import Flask        #flask에서 Flask class 임포트

app = Flask(__name__)          #Flask 객체를 생성 인자로 name(여기에는 경우에따라 달라서 단일 모듈일 때는 name을 쓴다)

@app.route('/')                #route()를 사용해 Flask에게 어떤 url이 함수를 실행시키는지 알려줌

def home():
       return 'Hello, world!'  #함수의 기능 설명

if __name__=='__main__':       #run()함수를 사용하여 로컬 서버로 실행
    app.run()   
