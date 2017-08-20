from flask import  Flask, render_template, request, jsonify
from tamu import Tamu
app = Flask(__name__,static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    tamu = Tamu('CSCE')
    error,client = tamu.cas_login(request.args.get('NetID'),request.args.get('password'))
    return jsonify(error)

@app.route('/courses',methods=['POST','GET'])
def getClasses():
    tamu = Tamu(request.args.get('major'))
    datas= tamu.get_term_list()
    return jsonify(datas)

@app.route('/getYourCourses',methods=['GET'])
def getYourCourses():
    print("call getYourCourses")
    tamu= Tamu('CSCE')
    datas = tamu.get_your_courses()
    return jsonify(datas)

if __name__=='__main__':
    app.run(debug=True)
