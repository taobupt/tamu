from flask import  Flask, render_template, request, jsonify
from tamu import Tamu
app = Flask(__name__,static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    tamu = Tamu()
    error,client = tamu.cas_login(request.args.get('NetID'),request.args.get('password'))
    return jsonify(error)

@app.route('/courses')
def courses():
    return "hello world"

if __name__=='__main__':
    app.run(debug=True)
