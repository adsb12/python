
from flask import Flask, render_template, request, redirect
from riot import riot_crowl
from flask import flash
#함수 가져오기

app = Flask("riot")         #어플리케이션 패키지의 이름
db = {}                         # 데이터베이스 실제 db는 아님 성능 향상때매

@app.route("/")
def home():
  return render_template("home.html")       #기본루트

@app.route("/search")                               #검색
def search():
  name = request.args.get("name")             #작성한 이름들고오기
  if name == None or name == "":
    return redirect("/")                                #없으면 다시빽
  if name in db: 
    r_lists = db[name]                                 #db에 있으면 db있는거 뿌림
  else:
    rank,r_len = riot_crowl(name)                 #없으면 만든함수 호출
    r_lists = rank
    db[name] = r_lists 
  return render_template("search.html", name = name, r_lists=r_lists, r_len=r_len)      #html로 던짐

app.run("0.0.0.0")
