
from flask import Flask, render_template, request, redirect, send_file
from riot import riot_crowl


app = Flask("riot")
db = {} # 데이터베이스

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/search")
def search():
  name = request.args.get("name")
  if name == None:
    return redirect("/")
  if name in db: 
    r_lists = db[name]
  else:
    rank,r_len = riot_crowl(name)
    r_lists = rank
    db[name] = r_lists 
  return render_template("search.html", name = name, r_lists=r_lists, r_len=r_len)

@app.route("/export") # 데이터 다운로드
def export():
  name = request.args.get("name")
  if name == None:
    return redirect("/")
  if name not in db:
    return redirect(f"/search?name={name}")
  save_to_file(name, db[name])
  return send_file(f"{name}.csv", as_attachment=True)

app.run("0.0.0.0")
