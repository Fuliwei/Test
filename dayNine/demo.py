#coding:utf-8
from flask import Flask ,request ,render_template
import json
app=Flask(__name__)
@app.route('/')
@app.route("/index")
def index():
	return render_template("login.html")
@app.route("/list")
def list():
	user = {"id":'1',"name":'xiaohei',"age":100}
	return json.dumps({'code':0,'reslut':user})
@app.route("/add",methods=['GET','POST'])
def add():
	data = dict((k,v[0]) for k ,v in dict(request.form).items())
	print data
	return json.dumps({'code':0,'result':data})
if __name__ == "__main__":
	app.run(host="0.0.0.0",port=1010,debug=True)
