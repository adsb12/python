from flask import Flask        #flask���� Flask class ����Ʈ

app = Flask(__name__)          #Flask ��ü�� ���� ���ڷ� name(���⿡�� ��쿡���� �޶� ���� ����� ���� name�� ����)

@app.route('/')                #route()�� ����� Flask���� � url�� �Լ��� �����Ű���� �˷���

def home():
       return 'Hello, world!'  #�Լ��� ��� ����

if __name__=='__main__':       #run()�Լ��� ����Ͽ� ���� ������ ����
    app.run()   
