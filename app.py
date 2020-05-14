from flask import Flask, render_template, request, session, redirect, url_for
from models.signup import Signup
from models.post import Post
from models.active import Active
from common.database import Database
import sys

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        signup = Signup(username=username,email=email,password=password)
        Database.insert(collection="login",data=signup.json())
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        credentials = Database.find_one(collection='login',query = {'username':username})
        req_password = None
        if credentials != None:
            req_password = credentials.get('password')
            session['username'] = credentials.get('username')
            active = Active(username=session['username'])
            Database.insert(collection='active',data=active.json())
        if req_password == None:
            return render_template('login.html',message="No Account found, Signup first")
        elif password == req_password:
            return redirect(url_for('stories'))
        else:
            return render_template('login.html',message="Invalid Credentials. Try Again")
    return render_template('login.html')

@app.route('/stories',methods=["POST",'GET'])
def stories():
    username = session['username']
    print('hello1',file=sys.stderr)
    if request.method == 'POST':
        content = request.form['message']
        post = Post(username=username,content=content)
        Database.insert('feed',post.json())
        return redirect(url_for('stories'))
    
    return render_template('story.html',username=username,posts = Database.find(collection='feed',data={}),onlines = Database.find(collection='active',data={}))

@app.route('/logout')
def logout():
    Database.remove(collection='active',query={'username':session['username']})
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.secret_key = 'highlyconfidential'
    app.run(port=3000,debug=True)