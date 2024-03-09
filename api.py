from flask import Flask ,jsonify,request
import flask
import requests
from flask_cors import CORS
import warnings
warnings.filterwarnings("ignore")
app = Flask(__name__)


CORS(app)

@app.route('/qivrimsetl')
def default_check():
    return 'Working'

@app.route('/jarvis/sourceinfluencer', methods=['POST'])
def instagramdata():
    userParams = request.get_json()
    print(userParams)
    # source = sourceinfluencer()
    # output = source.main(userParams)
    print('output...')
    return {"statuscode":"200","message":"Kafka insertion initiated","statusmessage":"Success"}
if __name__=="__main__":
    # app.run(debug=False)
    app.run(host='0.0.0.0',port="8089")
