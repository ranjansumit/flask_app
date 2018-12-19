from flask import Flask, render_template,url_for,request,redirect
from createUser import createUser

app = Flask(__name__)
'''
@app.route('/')
def hello_world():
    return 'Hello, World!'
'''


@app.route('/index')
def index():
    
    return render_template('index.html')


@app.route('/result', methods=['GET','POST'])
def result():
    result = request.form
    output=createUser().parse_logic(result)
    return render_template("result.html",output = output)
    

if __name__ == '__main__':
   app.run(host='0.0.0.0')
